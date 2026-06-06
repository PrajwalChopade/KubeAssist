from pathlib import Path
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter

RAW_DIR = Path("data/raw")
CHUNK_DIR = Path("data/chunks")

CHUNK_DIR.mkdir(parents=True, exist_ok=True)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
)


def build_chunks(text: str, parent_id: str, metadata: dict) -> list[dict]:
    chunks = splitter.split_text(text)
    records = []

    for idx, chunk in enumerate(chunks):
        record = {
            "parent_id": parent_id,
            "chunk_id": f"{parent_id}_{idx}",
            "text": chunk,
        }

        if metadata:
            record.update(metadata)

        records.append(record)

    return records


def process_file(md_file: Path, metadata: dict | None = None) -> int:
    text = md_file.read_text(encoding="utf-8")
    parent_id = md_file.stem

    for existing in CHUNK_DIR.glob(f"{parent_id}_*.json"):
        existing.unlink()

    records = build_chunks(text, parent_id, metadata or {})
    for idx, record in enumerate(records):
        out_file = CHUNK_DIR / f"{parent_id}_{idx}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(record, f, ensure_ascii=False, indent=2)

    return len(records)


def process_all(raw_dir: Path = RAW_DIR) -> int:
    total = 0
    for txt_file in RAW_DIR.glob("*.txt"):
        total += process_file(txt_file)
    return total


if __name__ == "__main__":
    total = process_all(RAW_DIR)
    print(f"Chunking complete: {total} chunks")
