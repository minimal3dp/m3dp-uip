import sys
import os
import re

# Configuration: Files and folders to ignore to prevent context pollution
IGNORE_DIRS = {".git", "__pycache__", "node_modules", "venv", "env", ".idea", ".vscode"}
IGNORE_EXTS = {
    ".pyc",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
}


def compress_text(text):
    """
    Applies 'Telegraphic Style' compression:
    1. Removes comments.
    2. Collapses whitespace.
    3. Removes stop words.
    """
    # 1. Remove comments (handling # for Python and // for JS/C-like)
    text = re.sub(r"#.*", "", text)
    text = re.sub(r"//.*", "", text)

    # 2. Remove multiple spaces and newlines
    text = re.sub(r"\s+", " ", text).strip()

    # 3. Remove common "stop words"
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "is",
        "are",
        "was",
        "were",
        "of",
        "in",
        "on",
        "at",
        "to",
        "for",
        "with",
        "by",
        "that",
        "this",
        "it",
        "as",
        "from",
    }

    words = text.split()
    compressed_words = [w for w in words if w.lower() not in stop_words]

    return " ".join(compressed_words)


def process_file(filepath):
    """Reads a single file, compresses it, and prints the block."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            compressed = compress_text(content)
            # We add XML-style tags so the LLM knows where file boundaries are
            print(f"<file path='{filepath}'>")
            print(compressed)
            print(f"</file>")
    except Exception as e:
        print(f"")


def process_path(path):
    """Determines if path is a file or folder and acts accordingly."""
    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for file in files:
                if any(file.endswith(ext) for ext in IGNORE_EXTS):
                    continue
                filepath = os.path.join(root, file)
                process_file(filepath)
    else:
        print(f"Error: Path '{path}' does not exist.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compress_context.py <file_or_folder_path>")
        sys.exit(1)

    target_path = sys.argv[1]
    process_path(target_path)
