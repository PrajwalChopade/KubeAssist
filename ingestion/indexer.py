import json
from pathlib import Path

from crawler.change_detector import get_hash
from ingestion.chunker import process_file
from ingestion.load_qdrant import load_chunks
from retrieval.bm25 import reload_index
from vectordb.qdrant_manager import reset_collection

RAW_DIR = Path("data/raw")
CHUNK_DIR = Path("data/chunks")
HASH_INDEX = Path("data/processed/hash_index.json")


def _load_hash_index() -> dict:
    if HASH_INDEX.exists():
        try:
            return json.loads(HASH_INDEX.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def _save_hash_index(index: dict) -> None:
    HASH_INDEX.parent.mkdir(parents=True, exist_ok=True)
    HASH_INDEX.write_text(json.dumps(index, indent=2), encoding="utf-8")


def _load_metadata(md_file: Path) -> dict:
    meta_file = md_file.with_suffix(".json")
    if meta_file.exists():
        try:
            return json.loads(meta_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def reindex(force: bool = False) -> dict:
    hash_index = _load_hash_index()
    updated = 0
    skipped = 0

    for md_file in RAW_DIR.glob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        doc_hash = get_hash(text)
        metadata = _load_metadata(md_file)

        key = metadata.get("url") or md_file.stem
        if not force and hash_index.get(key) == doc_hash:
            skipped += 1
            continue

        process_file(md_file, metadata)
        hash_index[key] = doc_hash
        updated += 1

    _save_hash_index(hash_index)

    reset_collection()
    loaded = load_chunks(CHUNK_DIR)
    reload_index()

    return {
        "updated": updated,
        "skipped": skipped,
        "chunks_loaded": loaded,
    }
