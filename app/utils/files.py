from pathlib import Path
import re
import shutil
import uuid

from fastapi import HTTPException, UploadFile, status

from app.config import get_settings


ALLOWED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg",
    ".pdf", ".mp4", ".webm",
}


def safe_filename(filename: str) -> str:
    stem = Path(filename).stem
    suffix = Path(filename).suffix.lower()
    cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "-", stem).strip("-") or "upload"
    return f"{cleaned}-{uuid.uuid4().hex[:10]}{suffix}"


def save_upload(upload: UploadFile, folder: str = "media") -> tuple[str, int, str]:
    settings = get_settings()
    suffix = Path(upload.filename or "").suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")

    destination_dir = settings.UPLOAD_DIR / folder
    destination_dir.mkdir(parents=True, exist_ok=True)
    filename = safe_filename(upload.filename or "upload")
    destination = destination_dir / filename

    size = 0
    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    with destination.open("wb") as buffer:
        while chunk := upload.file.read(1024 * 1024):
            size += len(chunk)
            if size > max_bytes:
                buffer.close()
                destination.unlink(missing_ok=True)
                raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File too large")
            buffer.write(chunk)

    rel_path = destination.relative_to(settings.BASE_DIR).as_posix()
    return f"/{rel_path}", size, suffix.lstrip(".")
