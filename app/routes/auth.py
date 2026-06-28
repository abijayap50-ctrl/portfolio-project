from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.auth.security import create_access_token, create_csrf_token, get_current_user, verify_password
from app.database import get_db
from app.models import User
from app.schemas import LoginRequest, Token, UserOut
from app.templating import templates


router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    response = templates.TemplateResponse("admin/login.html", {"request": request, "error": None})
    response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
    return response


@router.post("/login")
def login_form(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email, User.is_active.is_(True)).first()
    if not user or not verify_password(password, user.hashed_password):
        response = templates.TemplateResponse("admin/login.html", {"request": request, "error": "Invalid email or password"}, status_code=400)
        response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
        return response
    token = create_access_token(user.email, {"role": user.role})
    response = RedirectResponse("/admin", status_code=303)
    response.set_cookie("access_token", token, httponly=True, samesite="lax", max_age=60 * 60 * 8)
    response.set_cookie("csrf_token", create_csrf_token(), httponly=False, samesite="lax")
    return response


@router.post("/logout")
def logout():
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("access_token")
    response.delete_cookie("csrf_token")
    return response


@router.post("/api/login", response_model=Token)
def api_login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email, User.is_active.is_(True)).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return Token(access_token=create_access_token(user.email, {"role": user.role}))


@router.post("/api/logout")
def api_logout():
    return JSONResponse({"message": "Logged out. Delete the bearer token client-side."})


@router.get("/api/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user
