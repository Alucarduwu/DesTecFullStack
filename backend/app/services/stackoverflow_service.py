import requests
from datetime import datetime


STACKEXCHANGE_URL = (
    "https://api.stackexchange.com/2.2/search"
    "?order=desc&sort=activity&intitle=perl&site=stackoverflow"
)


def fetch_stackoverflow_items():
    response = requests.get(STACKEXCHANGE_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("items", [])


def format_date(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def map_question(item):
    owner = item.get("owner", {})

    return {
        "title": item.get("title"),
        "link": item.get("link"),
        "is_answered": item.get("is_answered"),
        "view_count": item.get("view_count", 0),
        "answer_count": item.get("answer_count", 0),
        "score": item.get("score", 0),
        "creation_date": format_date(item.get("creation_date", 0)),
        "last_activity_date": format_date(item.get("last_activity_date", 0)),
        "owner": {
            "display_name": owner.get("display_name", "Unknown"),
            "reputation": owner.get("reputation", 0),
            "profile_image": owner.get("profile_image"),
            "link": owner.get("link"),
        },
    }


def get_answered_summary():
    items = fetch_stackoverflow_items()

    answered = sum(1 for item in items if item.get("is_answered") is True)
    unanswered = sum(1 for item in items if item.get("is_answered") is False)

    return {
        "answered": answered,
        "unanswered": unanswered,
        "total": len(items),
    }


def get_highest_reputation_question():
    items = fetch_stackoverflow_items()

    if not items:
        return None

    question = max(
        items,
        key=lambda item: item.get("owner", {}).get("reputation", 0)
    )

    return map_question(question)


def get_lowest_views_question():
    items = fetch_stackoverflow_items()

    if not items:
        return None

    question = min(
        items,
        key=lambda item: item.get("view_count", 0)
    )

    return map_question(question)


def get_oldest_and_newest_questions():
    items = fetch_stackoverflow_items()

    if not items:
        return {
            "oldest": None,
            "newest": None,
        }

    oldest = min(items, key=lambda item: item.get("creation_date", 0))
    newest = max(items, key=lambda item: item.get("creation_date", 0))

    return {
        "oldest": map_question(oldest),
        "newest": map_question(newest),
    }


def get_console_report():
    highest_reputation = get_highest_reputation_question()
    lowest_views = get_lowest_views_question()
    oldest_newest = get_oldest_and_newest_questions()

    print("========== StackOverflow Report ==========")
    print("Pregunta con mayor reputación:")
    print(highest_reputation)
    print("------------------------------------------")
    print("Pregunta con menor número de vistas:")
    print(lowest_views)
    print("------------------------------------------")
    print("Pregunta más vieja:")
    print(oldest_newest.get("oldest"))
    print("------------------------------------------")
    print("Pregunta más actual:")
    print(oldest_newest.get("newest"))
    print("==========================================")

    return {
        "highest_reputation": highest_reputation,
        "lowest_views": lowest_views,
        "oldest": oldest_newest.get("oldest"),
        "newest": oldest_newest.get("newest"),
        "message": "Resultados impresos en consola correctamente",
    }