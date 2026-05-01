import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from './services/api';

type DashboardSection = 'home' | 'stackoverflow' | 'flights';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App implements OnInit {
  loading = true;
  errorMessage = '';
  data: any = null;

  activeSection: DashboardSection = 'home';
  expandedQuestion: string | null = null;
  isDarkMode = false;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadDashboard();
  }

  loadDashboard(): void {
    this.loading = true;
    this.errorMessage = '';

    console.log('[ANGULAR] Cargando dashboard');

    this.apiService.logFrontendEvent(
      'cargar_dashboard',
      this.activeSection,
      'El usuario solicitó cargar o actualizar la información del dashboard'
    ).subscribe();

    this.apiService.getDashboardData().subscribe({
      next: (response) => {
        this.data = response;
        this.loading = false;

        console.log('[ANGULAR] Dashboard cargado correctamente', response);

        this.apiService.logFrontendEvent(
          'dashboard_cargado',
          this.activeSection,
          'La información del dashboard se cargó correctamente',
          {
            stackoverflowTotal: response?.answeredSummary?.total,
            totalVuelos: response?.flightsSummary?.total_vuelos,
            answeredQuestions: response?.answeredSummary?.answered,
            unansweredQuestions: response?.answeredSummary?.unanswered
          }
        ).subscribe();
      },
      error: (error) => {
        console.error('[ANGULAR] Error loading dashboard:', error);

        this.errorMessage =
          'No se pudo cargar la información del backend. Verifica que Docker esté corriendo en el puerto 8000.';

        this.loading = false;

        this.apiService.logFrontendEvent(
          'error_dashboard',
          this.activeSection,
          'Ocurrió un error al cargar el dashboard',
          {
            error: error?.message || error
          }
        ).subscribe();
      }
    });
  }

  setSection(section: DashboardSection): void {
    this.activeSection = section;

    console.log('[ANGULAR] Cambio de sección:', section);

    this.apiService.logFrontendEvent(
      'cambio_seccion',
      section,
      `El usuario cambió a la sección ${section}`
    ).subscribe();

    if (section === 'stackoverflow') {
      this.expandedQuestion = 'stack-1';
      return;
    }

    if (section === 'flights') {
      this.expandedQuestion = 'flight-1';
      return;
    }

    this.expandedQuestion = null;
  }

  toggleQuestion(questionId: string): void {
    const wasOpen = this.expandedQuestion === questionId;
    this.expandedQuestion = wasOpen ? null : questionId;

    console.log('[ANGULAR] Toggle pregunta:', questionId, {
      opened: !wasOpen
    });

    this.apiService.logFrontendEvent(
      wasOpen ? 'cerrar_pregunta' : 'abrir_pregunta',
      this.activeSection,
      `El usuario ${wasOpen ? 'cerró' : 'abrió'} la pregunta ${questionId}`,
      {
        questionId,
        opened: !wasOpen
      }
    ).subscribe();
  }

  toggleTheme(): void {
    this.isDarkMode = !this.isDarkMode;

    console.log('[ANGULAR] Cambio de tema:', this.isDarkMode ? 'oscuro' : 'claro');

    this.apiService.logFrontendEvent(
      'cambio_tema',
      this.activeSection,
      `El usuario cambió al modo ${this.isDarkMode ? 'oscuro' : 'claro'}`,
      {
        darkMode: this.isDarkMode
      }
    ).subscribe();
  }

  openLink(url: string | undefined | null): void {
    if (!url) return;

    console.log('[ANGULAR] Abriendo link externo:', url);

    this.apiService.logFrontendEvent(
      'abrir_link_externo',
      this.activeSection,
      'El usuario abrió un link externo de StackOverflow',
      {
        url
      }
    ).subscribe();

    window.open(url, '_blank');
  }
}