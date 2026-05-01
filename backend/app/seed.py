from app.database import get_connection


def seed_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM aerolineas")
    total = cursor.fetchone()["total"]

    if total > 0:
        connection.close()
        return

    cursor.executemany(
        """
        INSERT INTO aerolineas (id_aerolinea, nombre_aerolinea)
        VALUES (?, ?)
        """,
        [
            (1, "Volaris"),
            (2, "Aeromar"),
            (3, "Interjet"),
            (4, "Aeromexico"),
        ]
    )

    cursor.executemany(
        """
        INSERT INTO aeropuertos (id_aeropuerto, nombre_aeropuerto)
        VALUES (?, ?)
        """,
        [
            (1, "Benito Juarez"),
            (2, "Guanajuato"),
            (3, "La paz"),
            (4, "Oaxaca"),
        ]
    )

    cursor.executemany(
        """
        INSERT INTO movimientos (id_movimiento, descripcion)
        VALUES (?, ?)
        """,
        [
            (1, "Salida"),
            (2, "Llegada"),
        ]
    )

    cursor.executemany(
        """
        INSERT INTO vuelos (id_aerolinea, id_aeropuerto, id_movimiento, dia)
        VALUES (?, ?, ?, ?)
        """,
        [
            (1, 1, 1, "2021-05-02"),
            (2, 1, 1, "2021-05-02"),
            (3, 2, 2, "2021-05-02"),
            (4, 3, 2, "2021-05-02"),
            (1, 3, 2, "2021-05-02"),
            (2, 1, 1, "2021-05-02"),
            (2, 3, 1, "2021-05-04"),
            (3, 4, 1, "2021-05-04"),
            (3, 4, 1, "2021-05-04"),
        ]
    )

    connection.commit()
    connection.close()