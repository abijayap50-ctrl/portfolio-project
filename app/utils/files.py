import base64
import os
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

    # Read the file content
    content = upload.file.read()
    size = len(content)
    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if size > max_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File too large")

    if os.getenv("VERCEL") or not settings.DATABASE_URL.startswith("sqlite"):
        mime_type = "image/png"
        if suffix == ".jpg" or suffix == ".jpeg":
            mime_type = "image/jpeg"
        elif suffix == ".gif":
            mime_type = "image/gif"
        elif suffix == ".webp":
            mime_type = "image/webp"
        elif suffix == ".svg":
            mime_type = "image/svg+xml"
        elif suffix == ".pdf":
            mime_type = "application/pdf"
        
        encoded = base64.b64encode(content).decode("utf-8")
        data_url = f"data:{mime_type};base64,{encoded}"
        return data_url, size, suffix.lstrip(".")

    destination_dir = settings.UPLOAD_DIR / folder
    destination_dir.mkdir(parents=True, exist_ok=True)
    filename = safe_filename(upload.filename or "upload")
    destination = destination_dir / filename

    with destination.open("wb") as buffer:
        buffer.write(content)

    rel_path = destination.relative_to(settings.BASE_DIR).as_posix()
    return f"/{rel_path}", size, suffix.lstrip(".")
