#!/usr/bin/env python3
"""
Convert PDFs in research/ to markdown for version control.

This script scans the research directory for PDF files and converts them
to markdown format using various extraction methods. The markdown files
are tracked in git while PDFs remain gitignored.

Usage:
    python scripts/convert_research_pdfs.py
    python scripts/convert_research_pdfs.py --file research/paper.pdf
    python scripts/convert_research_pdfs.py --watch  # Monitor for changes
"""

import argparse
import hashlib
import json
import subprocess  # nosec B404 - needed for pdftotext fallback
import sys
import time
from pathlib import Path

try:
    import pypdf
except ImportError:
    pypdf = None

try:
    import pymupdf  # PyMuPDF
except ImportError:
    pymupdf = None


class PDFConverter:
    """Convert PDF files to markdown with metadata tracking."""

    def __init__(self, research_dir: Path):
        self.research_dir = research_dir
        self.metadata_file = research_dir / ".conversion_metadata.json"
        self.metadata = self._load_metadata()

    def _load_metadata(self) -> dict:
        """Load conversion metadata to track processed files."""
        if self.metadata_file.exists():
            return json.loads(self.metadata_file.read_text())
        return {}

    def _save_metadata(self):
        """Save conversion metadata."""
        self.metadata_file.write_text(json.dumps(self.metadata, indent=2))

    def _get_file_hash(self, pdf_path: Path) -> str:
        """Calculate SHA256 hash of PDF file."""
        sha256 = hashlib.sha256()
        with open(pdf_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _needs_conversion(self, pdf_path: Path, md_path: Path) -> bool:
        """Check if PDF needs conversion (new or modified)."""
        if not md_path.exists():
            return True

        file_hash = self._get_file_hash(pdf_path)
        pdf_key = str(pdf_path.relative_to(self.research_dir))

        if pdf_key not in self.metadata:
            return True

        return self.metadata[pdf_key].get("hash") != file_hash

    def _extract_with_pymupdf(self, pdf_path: Path) -> str | None:
        """Extract text using PyMuPDF (best quality)."""
        if pymupdf is None:
            return None

        try:
            doc = pymupdf.open(pdf_path)
            text_blocks = []

            for page_num, page in enumerate(doc, 1):
                text_blocks.append(f"## Page {page_num}\n")
                text = page.get_text("text")
                text_blocks.append(text.strip())
                text_blocks.append("\n---\n")

            doc.close()
            return "\n\n".join(text_blocks)
        except Exception as e:
            print(f"  ⚠️  PyMuPDF extraction failed: {e}")
            return None

    def _extract_with_pypdf(self, pdf_path: Path) -> str | None:
        """Extract text using pypdf (fallback)."""
        if pypdf is None:
            return None

        try:
            reader = pypdf.PdfReader(pdf_path)
            text_blocks = []

            for page_num, page in enumerate(reader.pages, 1):
                text_blocks.append(f"## Page {page_num}\n")
                text = page.extract_text()
                text_blocks.append(text.strip())
                text_blocks.append("\n---\n")

            return "\n\n".join(text_blocks)
        except Exception as e:
            print(f"  ⚠️  pypdf extraction failed: {e}")
            return None

    def _extract_with_pdftotext(self, pdf_path: Path) -> str | None:
        """Extract text using pdftotext command (system fallback)."""
        try:
            # nosec B603,B607 - controlled input, pdftotext is a trusted system tool
            result = subprocess.run(
                ["pdftotext", "-layout", str(pdf_path), "-"],
                capture_output=True,
                text=True,
                timeout=30,
            )
            if result.returncode == 0:
                return result.stdout
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
        return None

    def convert_pdf(self, pdf_path: Path, force: bool = False) -> bool:
        """
        Convert a single PDF to markdown.

        Args:
            pdf_path: Path to PDF file
            force: Force conversion even if up-to-date

        Returns:
            True if conversion successful
        """
        md_path = pdf_path.with_suffix(".md")

        if not force and not self._needs_conversion(pdf_path, md_path):
            print(f"  ⏭️  Skipping {pdf_path.name} (up-to-date)")
            return True

        print(f"  🔄 Converting {pdf_path.name}...")

        # Try extraction methods in order of quality
        content = None
        method = None

        if content is None and pymupdf is not None:
            content = self._extract_with_pymupdf(pdf_path)
            method = "PyMuPDF"

        if content is None and pypdf is not None:
            content = self._extract_with_pypdf(pdf_path)
            method = "pypdf"

        if content is None:
            content = self._extract_with_pdftotext(pdf_path)
            method = "pdftotext"

        if content is None:
            print(f"  ❌ Failed to extract text from {pdf_path.name}")
            return False

        # Create markdown with metadata
        metadata_header = f"""# {pdf_path.stem}

> **Source:** `{pdf_path.name}`
> **Converted:** {time.strftime("%Y-%m-%d %H:%M:%S")}
> **Method:** {method}

---

"""
        markdown_content = metadata_header + content

        # Write markdown file
        md_path.write_text(markdown_content, encoding="utf-8")

        # Update metadata
        pdf_key = str(pdf_path.relative_to(self.research_dir))
        self.metadata[pdf_key] = {
            "hash": self._get_file_hash(pdf_path),
            "converted_at": time.time(),
            "method": method,
            "markdown": str(md_path.relative_to(self.research_dir)),
        }
        self._save_metadata()

        print(f"  ✅ Created {md_path.name}")
        return True

    def convert_all(self, force: bool = False) -> tuple[int, int]:
        """
        Convert all PDFs in research directory.

        Args:
            force: Force conversion of all files

        Returns:
            Tuple of (successful_count, total_count)
        """
        pdf_files = list(self.research_dir.rglob("*.pdf"))

        if not pdf_files:
            print("No PDF files found in research directory")
            return 0, 0

        print(f"\n📚 Found {len(pdf_files)} PDF file(s)")

        success = 0
        for pdf_path in pdf_files:
            if self.convert_pdf(pdf_path, force=force):
                success += 1

        return success, len(pdf_files)

    def watch(self, interval: int = 5):
        """
        Watch research directory for new/modified PDFs.

        Args:
            interval: Check interval in seconds
        """
        print(f"\n👁️  Watching {self.research_dir} for PDF changes...")
        print("Press Ctrl+C to stop\n")

        seen_pdfs = set(self.research_dir.rglob("*.pdf"))

        try:
            while True:
                time.sleep(interval)
                current_pdfs = set(self.research_dir.rglob("*.pdf"))

                # Check for new files
                new_pdfs = current_pdfs - seen_pdfs
                for pdf_path in new_pdfs:
                    print(f"\n📄 New PDF detected: {pdf_path.name}")
                    self.convert_pdf(pdf_path)

                # Check for modified files
                for pdf_path in current_pdfs:
                    if self._needs_conversion(pdf_path, pdf_path.with_suffix(".md")):
                        print(f"\n📝 Modified PDF detected: {pdf_path.name}")
                        self.convert_pdf(pdf_path)

                seen_pdfs = current_pdfs

        except KeyboardInterrupt:
            print("\n\n👋 Stopped watching")


def check_dependencies():
    """Check for available PDF extraction tools."""
    tools = []

    if pymupdf is not None:
        tools.append("✅ PyMuPDF (best quality)")
    else:
        tools.append("❌ PyMuPDF (install: pip install pymupdf)")

    if pypdf is not None:
        tools.append("✅ pypdf (good quality)")
    else:
        tools.append("❌ pypdf (install: pip install pypdf)")

    # Check for pdftotext
    try:
        # nosec B603,B607 - checking if system tool is available
        subprocess.run(["pdftotext", "-v"], capture_output=True, check=False, timeout=2)
        tools.append("✅ pdftotext (system tool)")
    except (subprocess.SubprocessError, FileNotFoundError):
        tools.append("❌ pdftotext (install: brew install poppler)")

    print("\n🔧 Available extraction tools:")
    for tool in tools:
        print(f"  {tool}")

    if not any("✅" in tool for tool in tools):
        print("\n⚠️  No extraction tools available!")
        print("Install at least one: pip install pymupdf")
        return False

    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Convert research PDFs to markdown for version control"
    )
    parser.add_argument("--file", type=Path, help="Convert a specific PDF file", metavar="PATH")
    parser.add_argument("--force", action="store_true", help="Force conversion even if up-to-date")
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch for new/modified PDFs and convert automatically",
    )
    parser.add_argument("--check", action="store_true", help="Check available extraction tools")
    parser.add_argument(
        "--interval", type=int, default=5, help="Watch interval in seconds (default: 5)"
    )

    args = parser.parse_args()

    # Find research directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    research_dir = project_root / "research"

    if not research_dir.exists():
        print(f"❌ Research directory not found: {research_dir}")
        sys.exit(1)

    if args.check:
        check_dependencies()
        sys.exit(0)

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    converter = PDFConverter(research_dir)

    if args.file:
        # Convert specific file
        pdf_path = Path(args.file)
        if not pdf_path.exists():
            print(f"❌ File not found: {pdf_path}")
            sys.exit(1)

        if pdf_path.suffix.lower() != ".pdf":
            print(f"❌ Not a PDF file: {pdf_path}")
            sys.exit(1)

        success = converter.convert_pdf(pdf_path, force=args.force)
        sys.exit(0 if success else 1)

    elif args.watch:
        # Watch mode
        converter.watch(interval=args.interval)

    else:
        # Convert all PDFs
        success, total = converter.convert_all(force=args.force)
        print(f"\n✨ Converted {success}/{total} files")
        sys.exit(0 if success == total else 1)


if __name__ == "__main__":
    main()
