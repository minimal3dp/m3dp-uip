#!/usr/bin/env python3
"""
Quick Vision AI Demo

This script demonstrates the vision service functionality without needing
to start the full backend server. It uses the VisionService directly.

Usage:
    python demo_vision.py path/to/image.jpg

Or use the built-in mock mode (doesn't call real API):
    VISION_MOCK_ENABLED=true python demo_vision.py path/to/image.jpg
"""

import asyncio
import sys
from pathlib import Path

# Add backend to Python path
backend_dir = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_dir))

from app.services.vision_service import VisionService  # noqa: E402


async def demo_vision_analysis(image_path: str | None = None):
    """Demonstrate vision service with a sample image or mock data."""

    print("\n" + "=" * 60)
    print("  M3DP Vision AI Demo")
    print("=" * 60 + "\n")

    # Initialize service
    service = VisionService()

    # Check if configured
    if service.is_configured():
        print("✅ Vision service configured (API key found)")
        print("📡 Using model: Gemini 1.5 Pro")
    else:
        print("⚠️  No API key found - using mock mode")

    # Load image or use fake data
    if image_path:
        print(f"📁 Loading image: {image_path}")
        try:
            with open(image_path, "rb") as f:
                image_data = f.read()
            print(f"✅ Image loaded: {len(image_data):,} bytes")
        except FileNotFoundError:
            print(f"❌ Error: File not found: {image_path}")
            return
    else:
        print("ℹ️  No image provided - using test data")
        image_data = b"fake-test-image-data"

    # Optional context (improves accuracy)
    context = {
        "printer_model": "Ender 3 V2",
        "filament_type": "PLA",
        "filament_color": "Black",
        "nozzle_size": 0.4,
    }

    print("\n📋 Context:")
    for key, value in context.items():
        print(f"   {key}: {value}")

    print("\n🔍 Analyzing image...")

    try:
        # Analyze image
        result = await service.analyze_image(image_data, context)

        # Display results
        print("\n" + "=" * 60)
        print("  ANALYSIS RESULTS")
        print("=" * 60 + "\n")

        print(f"🏷️  Classification: {result['classification']}")
        print(f"📊 Issue Type: {result['issue_type']}")
        print(f"🎯 Confidence: {result['confidence']:.1%}")

        print("\n👁️  Observations:")
        for i, obs in enumerate(result["observations"], 1):
            print(f"   {i}. {obs}")

        print("\n🔧 Likely Causes:")
        for i, cause in enumerate(result["likely_causes"], 1):
            print(f"   {i}. {cause}")

        if "csv_reference" in result:
            print(f"\n📚 CSV Reference: {result['csv_reference']}")
            if "csv_specific" in result:
                print(f"   Specific file: {result['csv_specific']}")

        # Confidence warning
        if result["confidence"] < 0.6:
            print("\n⚠️  Low confidence detected!")
            print("   Consider providing more context or uploading multiple images")

        print("\n" + "=" * 60 + "\n")
        print("✅ Analysis complete!")

    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("   Make sure GOOGLE_GENAI_API_KEY is set in .env")
    except RuntimeError as e:
        print(f"\n❌ API Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {type(e).__name__}: {e}")


def main():
    """Main entry point."""

    # Get image path from command line
    image_path = sys.argv[1] if len(sys.argv) > 1 else None

    if not image_path:
        print("\nUsage: python demo_vision.py path/to/image.jpg")
        print("\nOr run with mock mode (no API calls):")
        print("  VISION_MOCK_ENABLED=true python demo_vision.py\n")

        # Continue with demo even without image
        response = input("Continue with demo anyway? [y/N] ")
        if response.lower() != "y":
            print("Exiting...")
            return

    # Run async function
    asyncio.run(demo_vision_analysis(image_path))


if __name__ == "__main__":
    main()
