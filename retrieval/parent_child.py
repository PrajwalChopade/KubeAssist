from pathlib import Path
import json

RAW_DIR = Path("data/raw")


def get_parent_doc(parent_id: str) -> str:
    file = RAW_DIR / f"{parent_id}.md"
    if file.exists():
        return file.read_text(encoding="utf-8")
    return ""


def get_parent_info(parent_id: str) -> dict:
    md_file = RAW_DIR / f"{parent_id}.md"
    meta_file = RAW_DIR / f"{parent_id}.json"

    info = {
        "text": "",
        "url": "",
        "title": "",
    }

    if md_file.exists():
        info["text"] = md_file.read_text(encoding="utf-8")

    if meta_file.exists():
        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            info["url"] = meta.get("url", "")
            info["title"] = meta.get("title", "")
        except json.JSONDecodeError:
            pass

    return info
