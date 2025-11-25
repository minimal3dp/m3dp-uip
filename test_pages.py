#!/usr/bin/env python3
"""Test script to verify all Python frontend pages are working"""

import subprocess  # nosec B404
import sys
import time


def test_pages():
    print("🚀 Starting test server...")

    # Start server
    proc = subprocess.Popen(
        ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        cwd="backend",
    )

    try:
        print("⏳ Waiting for server to start...")
        time.sleep(6)

        import requests

        pages = [
            ("/home", "Home page"),
            ("/calculators-ui", "Calculators list"),
            ("/diagnosis-ui", "Diagnosis page"),
            ("/calculators/rotation-distance-ui", "Rotation Distance calculator"),
            ("/calculators/pressure-advance-ui", "Pressure Advance calculator"),
            ("/calculators/max-volumetric-speed-ui", "Max Volumetric Speed calculator"),
        ]

        print("\n📄 Testing pages...")
        print("-" * 60)

        passed = 0
        failed = 0

        for path, name in pages:
            try:
                r = requests.get(f"http://localhost:8000{path}", timeout=5)
                if r.status_code == 200:
                    print(f"✅ {name:40s} OK")
                    passed += 1
                else:
                    print(f"❌ {name:40s} Failed ({r.status_code})")
                    failed += 1
            except Exception as e:
                print(f"❌ {name:40s} Error: {e}")
                failed += 1

        print("-" * 60)
        print(f"\n📊 Results: {passed} passed, {failed} failed")

        return failed == 0

    finally:
        print("\n🛑 Stopping server...")
        proc.terminate()
        proc.wait()
        print("✅ Done!")


if __name__ == "__main__":
    success = test_pages()
    sys.exit(0 if success else 1)
