from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


def nl2br(value: str | None) -> str:
    return "" if not value else "<br>".join(value.splitlines())


def tags(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.replace("\n", ",").split(",") if part.strip()]


templates.env.filters["nl2br"] = nl2br
templates.env.filters["tags"] = tags
