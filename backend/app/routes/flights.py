from fastapi import APIRouter, HTTPException

from app.services.flights_service import (
    get_airlines,
    get_airports,
    get_movements,
    get_all_flights,
    get_flights_summary,
    get_flights_by_airline,
    get_flights_by_airport,
    get_flights_by_day,
    get_top_airport,
    get_top_airlines,
    get_busiest_days,
    get_airlines_more_than_two_flights_per_day,
)

router = APIRouter()


@router.get("/airlines")
def airlines():
    try:
        return get_airlines()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/airports")
def airports():
    try:
        return get_airports()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/movements")
def movements():
    try:
        return get_movements()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/all")
def all_flights():
    try:
        return get_all_flights()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/summary")
def flights_summary():
    try:
        return get_flights_summary()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/by-airline")
def flights_by_airline():
    try:
        return get_flights_by_airline()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/by-airport")
def flights_by_airport():
    try:
        return get_flights_by_airport()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/by-day")
def flights_by_day():
    try:
        return get_flights_by_day()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/top-airport")
def top_airport():
    try:
        return get_top_airport()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/top-airline")
def top_airline():
    try:
        return get_top_airlines()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/busiest-day")
def busiest_day():
    try:
        return get_busiest_days()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/airlines-more-than-two-flights-per-day")
def airlines_more_than_two_flights_per_day():
    try:
        return get_airlines_more_than_two_flights_per_day()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))