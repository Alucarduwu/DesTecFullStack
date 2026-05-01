from app.database import get_connection


def rows_to_dict_list(rows):
    return [dict(row) for row in rows]


def get_airlines():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            id_aerolinea,
            nombre_aerolinea
        FROM aerolineas
        ORDER BY id_aerolinea;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_airports():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            id_aeropuerto,
            nombre_aeropuerto
        FROM aeropuertos
        ORDER BY id_aeropuerto;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_movements():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            id_movimiento,
            descripcion
        FROM movimientos
        ORDER BY id_movimiento;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_all_flights():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            v.id_vuelo,
            a.nombre_aerolinea,
            ap.nombre_aeropuerto,
            m.descripcion AS movimiento,
            v.dia
        FROM vuelos v
        JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
        JOIN aeropuertos ap ON v.id_aeropuerto = ap.id_aeropuerto
        JOIN movimientos m ON v.id_movimiento = m.id_movimiento
        ORDER BY v.dia, v.id_vuelo;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_flights_summary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) AS total_vuelos FROM vuelos;")
    total_flights = cursor.fetchone()["total_vuelos"]

    cursor.execute("SELECT COUNT(*) AS total_aerolineas FROM aerolineas;")
    total_airlines = cursor.fetchone()["total_aerolineas"]

    cursor.execute("SELECT COUNT(*) AS total_aeropuertos FROM aeropuertos;")
    total_airports = cursor.fetchone()["total_aeropuertos"]

    cursor.execute("SELECT COUNT(*) AS total_movimientos FROM movimientos;")
    total_movements = cursor.fetchone()["total_movimientos"]

    connection.close()

    return {
        "total_vuelos": total_flights,
        "total_aerolineas": total_airlines,
        "total_aeropuertos": total_airports,
        "total_tipos_movimiento": total_movements,
    }


def get_flights_by_airline():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            a.nombre_aerolinea,
            COUNT(*) AS total_vuelos
        FROM vuelos v
        JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
        GROUP BY a.id_aerolinea, a.nombre_aerolinea
        ORDER BY total_vuelos DESC, a.nombre_aerolinea;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_flights_by_airport():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            ap.nombre_aeropuerto,
            COUNT(*) AS total_movimientos
        FROM vuelos v
        JOIN aeropuertos ap ON v.id_aeropuerto = ap.id_aeropuerto
        GROUP BY ap.id_aeropuerto, ap.nombre_aeropuerto
        ORDER BY total_movimientos DESC, ap.nombre_aeropuerto;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_flights_by_day():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            dia,
            COUNT(*) AS total_vuelos
        FROM vuelos
        GROUP BY dia
        ORDER BY dia;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_top_airport():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        WITH conteo AS (
            SELECT 
                ap.nombre_aeropuerto,
                COUNT(*) AS total_movimientos
            FROM vuelos v
            JOIN aeropuertos ap ON v.id_aeropuerto = ap.id_aeropuerto
            GROUP BY ap.id_aeropuerto, ap.nombre_aeropuerto
        ),
        maximo AS (
            SELECT MAX(total_movimientos) AS max_movimientos
            FROM conteo
        )
        SELECT 
            c.nombre_aeropuerto,
            c.total_movimientos
        FROM conteo c
        JOIN maximo m ON c.total_movimientos = m.max_movimientos
        ORDER BY c.nombre_aeropuerto;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_top_airlines():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        WITH conteo AS (
            SELECT 
                a.nombre_aerolinea,
                COUNT(*) AS total_vuelos
            FROM vuelos v
            JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
            GROUP BY a.id_aerolinea, a.nombre_aerolinea
        ),
        maximo AS (
            SELECT MAX(total_vuelos) AS max_vuelos
            FROM conteo
        )
        SELECT 
            c.nombre_aerolinea,
            c.total_vuelos
        FROM conteo c
        JOIN maximo m ON c.total_vuelos = m.max_vuelos
        ORDER BY c.nombre_aerolinea;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_busiest_days():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        WITH conteo AS (
            SELECT 
                dia,
                COUNT(*) AS total_vuelos
            FROM vuelos
            GROUP BY dia
        ),
        maximo AS (
            SELECT MAX(total_vuelos) AS max_vuelos
            FROM conteo
        )
        SELECT 
            c.dia,
            c.total_vuelos
        FROM conteo c
        JOIN maximo m ON c.total_vuelos = m.max_vuelos
        ORDER BY c.dia;
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows_to_dict_list(rows)


def get_airlines_more_than_two_flights_per_day():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            a.nombre_aerolinea,
            v.dia,
            COUNT(*) AS total_vuelos
        FROM vuelos v
        JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
        GROUP BY a.nombre_aerolinea, v.dia
        HAVING COUNT(*) > 2
        ORDER BY v.dia, total_vuelos DESC;
    """)

    rows = cursor.fetchall()
    connection.close()

    result = rows_to_dict_list(rows)

    return {
        "criteria": "Aerolíneas con más de 2 vuelos en un mismo día",
        "results": result,
        "message": "No se encontraron aerolíneas con más de 2 vuelos en un mismo día."
        if len(result) == 0
        else "Consulta ejecutada correctamente."
    }