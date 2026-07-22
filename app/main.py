from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles

from app.config import get_settings
from app.database import Base, SessionLocal, engine
from app.routes import admin, api, auth, public
from app.services.content import ensure_default_content, ensure_default_superuser


settings = get_settings()
app = FastAPI(title=settings.PROJECT_NAME)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code in {status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN}:
        if request.url.path.startswith("/admin"):
            return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers=exc.headers,
    )


app.include_router(auth.router)
app.include_router(public.router)
app.include_router(admin.router)
app.include_router(api.router)


@app.on_event("startup")
def startup() -> None:
    try:
        settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        ensure_default_superuser(db)
        ensure_default_content(db)
    finally:
        db.close()

