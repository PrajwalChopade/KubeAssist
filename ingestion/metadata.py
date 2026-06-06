from pathlib import Path


def extract_metadata(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    title = text.split("\n")[0] if text else ""

    return {
        "title": title,
        "section": path.parent.name,
    }
