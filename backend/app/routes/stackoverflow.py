from datetime import datetime
from typing import Any, Dict, List

import requests
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/api/stackoverflow",
    tags=["StackOverflow"]
)

STACKOVERFLOW_URL = (
    "https://api.stackexchange.com/2.2/search"
    "?order=desc&sort=activity&intitle=perl&site=stackoverflow"
)


def _fetch_stackoverflow_items() -> List[Dict[str, Any]]:
    try:
        response = requests.get(STACKOVERFLOW_URL, timeout=15)
        response.raise_for_status()
        payload = response.json()
        return payload.get("items", [])
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail=f"No se pudo consumir StackExchange API: {str(error)}"
        )


def _format_date(timestamp: int | None) -> str:
    if not timestamp:
        return "Fecha no disponible"

    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def _normalize_question(item: Dict[str, Any]) -> Dict[str, Any]:
    owner = item.get("owner", {}) or {}

    return {
        "title": item.get("title", "Sin título"),
        "link": item.get("link", ""),
        "is_answered": item.get("is_answered", False),
        "view_count": item.get("view_count", 0),
        "answer_count": item.get("answer_count", 0),
        "score": item.get("score", 0),
        "creation_date": _format_date(item.get("creation_date")),
        "last_activity_date": _format_date(item.get("last_activity_date")),
        "owner": {
            "display_name": owner.get("display_name", "Usuario no disponible"),
            "reputation": owner.get("reputation", 0),
            "profile_image": owner.get("profile_image", ""),
            "link": owner.get("link", "")
        }
    }


def _get_answered_summary(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    answered = sum(1 for item in items if item.get("is_answered") is True)
    unanswered = len(items) - answered

    return {
        "answered": answered,
        "unanswered": unanswered,
        "total": len(items)
    }


def _get_highest_reputation_question(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not items:
        raise HTTPException(status_code=404, detail="No hay datos de StackOverflow")

    question = max(
        items,
        key=lambda item: (item.get("owner", {}) or {}).get("reputation", 0)
    )

    return _normalize_question(question)


def _get_lowest_views_question(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not items:
        raise HTTPException(status_code=404, detail="No hay datos de StackOverflow")

    question = min(
        items,
        key=lambda item: item.get("view_count", 0)
    )

    return _normalize_question(question)


def _get_oldest_newest_questions(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not items:
        raise HTTPException(status_code=404, detail="No hay datos de StackOverflow")

    oldest = min(
        items,
        key=lambda item: item.get("creation_date", 0)
    )

    newest = max(
        items,
        key=lambda item: item.get("creation_date", 0)
    )

    return {
        "oldest": _normalize_question(oldest),
        "newest": _normalize_question(newest)
    }


@router.get("/answered-summary")
def answered_summary():
    items = _fetch_stackoverflow_items()
    return _get_answered_summary(items)


@router.get("/highest-reputation")
def highest_reputation():
    items = _fetch_stackoverflow_items()
    return _get_highest_reputation_question(items)


@router.get("/lowest-views")
def lowest_views():
    items = _fetch_stackoverflow_items()
    return _get_lowest_views_question(items)


@router.get("/oldest-newest")
def oldest_newest():
    items = _fetch_stackoverflow_items()
    return _get_oldest_newest_questions(items)


@router.get("/console-report")
def console_report():
    items = _fetch_stackoverflow_items()

    highest = _get_highest_reputation_question(items)
    lowest = _get_lowest_views_question(items)
    oldest_newest_data = _get_oldest_newest_questions(items)

    oldest = oldest_newest_data["oldest"]
    newest = oldest_newest_data["newest"]

    print("\n")
    print("====================================================")
    print("REPORTE STACKOVERFLOW - RETO TÉCNICO CASA MECATE")
    print("====================================================")

    print("\n[PUNTO 2] Pregunta asociada al usuario con mayor reputación:")
    print(f"Título: {highest.get('title')}")
    print(f"Usuario: {highest.get('owner', {}).get('display_name')}")
    print(f"Reputación: {highest.get('owner', {}).get('reputation')}")
    print(f"Link: {highest.get('link')}")

    print("\n[PUNTO 3] Pregunta con menor número de vistas:")
    print(f"Título: {lowest.get('title')}")
    print(f"Vistas: {lowest.get('view_count')}")
    print(f"Link: {lowest.get('link')}")

    print("\n[PUNTO 4] Pregunta más vieja:")
    print(f"Título: {oldest.get('title')}")
    print(f"Fecha de creación: {oldest.get('creation_date')}")
    print(f"Link: {oldest.get('link')}")

    print("\n[PUNTO 4] Pregunta más actual:")
    print(f"Título: {newest.get('title')}")
    print(f"Fecha de creación: {newest.get('creation_date')}")
    print(f"Link: {newest.get('link')}")

    print("====================================================")
    print("FIN DEL REPORTE STACKOVERFLOW")
    print("====================================================")
    print("\n")

    return {
        "message": "Resultados impresos en consola correctamente",
        "printed": True,
        "where_to_verify": "Docker Desktop → Containers → backend → Logs, o en la terminal donde corre Uvicorn.",
        "report": {
            "highest_reputation": highest,
            "lowest_views": lowest,
            "oldest": oldest,
            "newest": newest
        }
    }


@router.get("/oldest")
def oldest_question():
    items = _fetch_stackoverflow_items()
    return _get_oldest_newest_questions(items)["oldest"]


@router.get("/newest")
def newest_question():
    items = _fetch_stackoverflow_items()
    return _get_oldest_newest_questions(items)["newest"]