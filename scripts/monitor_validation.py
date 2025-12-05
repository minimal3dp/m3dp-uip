#!/usr/bin/env python3
"""Monitor validation progress in real-time."""

import json
import time
from pathlib import Path

REPORT_PATH = Path("backend/reports/vision_validation_report.json")
TOTAL_IMAGES = 6237


def format_time(seconds):
    """Format seconds into human-readable time."""
    if seconds < 60:
        return f"{seconds:.0f}s"
    elif seconds < 3600:
        mins = seconds / 60
        return f"{mins:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"


def monitor():
    """Monitor validation progress."""
    print("🔍 Monitoring validation progress...")
    print(f"📊 Total images: {TOTAL_IMAGES}")
    print(f"📁 Report path: {REPORT_PATH}")
    print("-" * 60)

    last_count = 0
    start_time = time.time()
    last_update_time = start_time

    while True:
        try:
            if REPORT_PATH.exists():
                with open(REPORT_PATH) as f:
                    report = json.load(f)

                current_count = report.get("total_images", 0)
                correct = report.get("correct_predictions", 0)
                accuracy = report.get("accuracy", 0) * 100

                # Calculate progress
                progress_pct = (current_count / TOTAL_IMAGES) * 100
                remaining = TOTAL_IMAGES - current_count

                # Calculate rate and ETA
                elapsed = time.time() - start_time
                if current_count > 0:
                    rate = current_count / elapsed  # images per second
                    eta_seconds = remaining / rate if rate > 0 else 0
                else:
                    rate = 0
                    eta_seconds = 0

                # Show update if progress changed
                if current_count != last_count:
                    last_update_time = time.time()
                    print(f"\r⏳ Progress: {current_count}/{TOTAL_IMAGES} ({progress_pct:.1f}%) | "
                          f"✓ Correct: {correct} ({accuracy:.1f}%) | "
                          f"⚡ Rate: {rate:.1f} img/s | "
                          f"⏱️  ETA: {format_time(eta_seconds)}", end="", flush=True)
                    last_count = current_count

                # Check if complete
                if current_count >= TOTAL_IMAGES:
                    print("\n" + "=" * 60)
                    print("✅ VALIDATION COMPLETE!")
                    print("=" * 60)
                    print(f"📊 Total Images: {current_count}")
                    print(f"✓ Correct Predictions: {correct}")
                    print(f"📈 Overall Accuracy: {accuracy:.2f}%")
                    print(f"⏱️  Total Time: {format_time(elapsed)}")
                    print("\n📋 Per-Defect Breakdown:")

                    by_defect = report.get("by_defect_type", {})
                    for defect, stats in sorted(by_defect.items()):
                        defect_acc = stats.get("accuracy", 0) * 100
                        defect_total = stats.get("total", 0)
                        defect_correct = stats.get("correct", 0)
                        status = "✅" if defect_acc >= 70 else "⚠️"
                        print(f"  {status} {defect:20s}: {defect_correct}/{defect_total} ({defect_acc:.1f}%)")

                    print(f"\n📄 Full report: {REPORT_PATH}")
                    break

            else:
                print("\r⏳ Waiting for validation to start...", end="", flush=True)

            # Check for stalled progress (no update in 60 seconds)
            if last_count > 0 and time.time() - last_update_time > 60:
                print("\n⚠️  Warning: No progress in 60 seconds. Validation may have stalled.")

            time.sleep(2)  # Update every 2 seconds

        except KeyboardInterrupt:
            print("\n\n⏸️  Monitoring stopped by user")
            print(f"Last known progress: {last_count}/{TOTAL_IMAGES} images")
            break
        except json.JSONDecodeError:
            # Report file being written, try again
            time.sleep(1)
            continue
        except Exception as e:
            print(f"\n❌ Error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    monitor()
