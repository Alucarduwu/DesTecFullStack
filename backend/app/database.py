import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "flights.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aerolineas (
            id_aerolinea INTEGER PRIMARY KEY,
            nombre_aerolinea TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aeropuertos (
            id_aeropuerto INTEGER PRIMARY KEY,
            nombre_aeropuerto TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id_movimiento INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vuelos (
            id_vuelo INTEGER PRIMARY KEY AUTOINCREMENT,
            id_aerolinea INTEGER NOT NULL,
            id_aeropuerto INTEGER NOT NULL,
            id_movimiento INTEGER NOT NULL,
            dia TEXT NOT NULL,
            FOREIGN KEY (id_aerolinea) REFERENCES aerolineas(id_aerolinea),
            FOREIGN KEY (id_aeropuerto) REFERENCES aeropuertos(id_aeropuerto),
            FOREIGN KEY (id_movimiento) REFERENCES movimientos(id_movimiento)
        );
    """)

    connection.commit()
    connection.close()