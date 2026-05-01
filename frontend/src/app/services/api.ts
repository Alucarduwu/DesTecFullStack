import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, forkJoin, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly apiUrl = 'https://localhost:8000';

  constructor(private http: HttpClient) {}

  private safeGet<T>(endpoint: string, fallback: T) {
    const url = `${this.apiUrl}${endpoint}`;

    return this.http.get<T>(url).pipe(
      catchError((error) => {
        console.error(`[API ERROR] Endpoint falló: ${url}`, error);
        return of(fallback);
      })
    );
  }

  logFrontendEvent(
    action: string,
    section: string,
    detail: string,
    metadata: any = {}
  ) {
    const url = `${this.apiUrl}/api/logs/frontend-event`;

    return this.http.post(url, {
      action,
      section,
      detail,
      metadata,
      timestamp: new Date().toISOString()
    }).pipe(
      catchError((error) => {
        console.error('[LOG ERROR] No se pudo enviar el log de frontend:', error);
        return of(null);
      })
    );
  }

  // =========================
  // StackOverflow endpoints
  // =========================

  getStackOverflowAnsweredSummary() {
    return this.safeGet('/api/stackoverflow/answered-summary', {
      answered: 0,
      unanswered: 0,
      total: 0
    });
  }

  getStackOverflowHighestReputation() {
    return this.safeGet('/api/stackoverflow/highest-reputation', {
      title: 'No disponible',
      link: '',
      is_answered: false,
      view_count: 0,
      answer_count: 0,
      score: 0,
      creation_date: 'No disponible',
      last_activity_date: 'No disponible',
      owner: {
        display_name: 'No disponible',
        reputation: 0,
        profile_image: '',
        link: ''
      }
    });
  }

  getStackOverflowLowestViews() {
    return this.safeGet('/api/stackoverflow/lowest-views', {
      title: 'No disponible',
      link: '',
      is_answered: false,
      view_count: 0,
      answer_count: 0,
      score: 0,
      creation_date: 'No disponible',
      last_activity_date: 'No disponible',
      owner: {
        display_name: 'No disponible',
        reputation: 0,
        profile_image: '',
        link: ''
      }
    });
  }

  getStackOverflowOldestNewest() {
    return this.safeGet('/api/stackoverflow/oldest-newest', {
      oldest: {
        title: 'No disponible',
        link: '',
        is_answered: false,
        view_count: 0,
        answer_count: 0,
        score: 0,
        creation_date: 'No disponible',
        last_activity_date: 'No disponible',
        owner: {
          display_name: 'No disponible',
          reputation: 0,
          profile_image: '',
          link: ''
        }
      },
      newest: {
        title: 'No disponible',
        link: '',
        is_answered: false,
        view_count: 0,
        answer_count: 0,
        score: 0,
        creation_date: 'No disponible',
        last_activity_date: 'No disponible',
        owner: {
          display_name: 'No disponible',
          reputation: 0,
          profile_image: '',
          link: ''
        }
      }
    });
  }

  getStackOverflowConsoleReport() {
    return this.safeGet('/api/stackoverflow/console-report', {
      message: 'No se pudo ejecutar el reporte en consola',
      printed: false,
      where_to_verify: 'Revisar logs del backend',
      report: null
    });
  }

  getStackOverflowOldest() {
    return this.safeGet('/api/stackoverflow/oldest', {
      title: 'No disponible',
      link: '',
      creation_date: 'No disponible'
    });
  }

  getStackOverflowNewest() {
    return this.safeGet('/api/stackoverflow/newest', {
      title: 'No disponible',
      link: '',
      creation_date: 'No disponible'
    });
  }

  // =========================
  // Flights endpoints
  // =========================

  getFlightsAirlines() {
    return this.safeGet('/api/flights/airlines', []);
  }

  getFlightsAirports() {
    return this.safeGet('/api/flights/airports', []);
  }

  getFlightsMovements() {
    return this.safeGet('/api/flights/movements', []);
  }

  getFlightsTopAirport() {
    return this.safeGet('/api/flights/top-airport', []);
  }

  getFlightsTopAirline() {
    return this.safeGet('/api/flights/top-airline', []);
  }

  getFlightsBusiestDay() {
    return this.safeGet('/api/flights/busiest-day', []);
  }

  getFlightsMoreThanTwoPerDay() {
    return this.safeGet('/api/flights/airlines-more-than-two-flights-per-day', {
      results: [],
      message: 'No hay aerolíneas que cumplan esta condición.'
    });
  }

  getFlightsSummary() {
    return this.safeGet('/api/flights/summary', {
      total_vuelos: 0,
      total_aerolineas: 0,
      total_aeropuertos: 0,
      total_movimientos: 0
    });
  }

  getAllFlights() {
    return this.safeGet('/api/flights/all', []);
  }

  getFlightsByAirline() {
    return this.safeGet('/api/flights/by-airline', []);
  }

  getFlightsByAirport() {
    return this.safeGet('/api/flights/by-airport', []);
  }

  getFlightsByDay() {
    return this.safeGet('/api/flights/by-day', []);
  }

  // =========================
  // Dashboard data
  // =========================

  getDashboardData() {
    return forkJoin({
      answeredSummary: this.getStackOverflowAnsweredSummary(),
      highestReputation: this.getStackOverflowHighestReputation(),
      lowestViews: this.getStackOverflowLowestViews(),
      oldestNewest: this.getStackOverflowOldestNewest(),
      consoleReport: this.getStackOverflowConsoleReport(),

      oldest: this.getStackOverflowOldest(),
      newest: this.getStackOverflowNewest(),

      airlines: this.getFlightsAirlines(),
      airports: this.getFlightsAirports(),
      movements: this.getFlightsMovements(),

      topAirport: this.getFlightsTopAirport(),
      topAirline: this.getFlightsTopAirline(),
      busiestDay: this.getFlightsBusiestDay(),
      moreThanTwoPerDay: this.getFlightsMoreThanTwoPerDay(),

      flightsSummary: this.getFlightsSummary(),
      allFlights: this.getAllFlights(),
      flightsByAirline: this.getFlightsByAirline(),
      flightsByAirport: this.getFlightsByAirport(),
      flightsByDay: this.getFlightsByDay()
    });
  }
}