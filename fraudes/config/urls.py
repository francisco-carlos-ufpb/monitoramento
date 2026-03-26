
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import LicitacaoViewSet, FraudeGuiaView, FraudeGuiaRawView, FraudeRelatorioView, HomeView

router = DefaultRouter()
router.register(r'licitacoes', LicitacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('guia/', FraudeGuiaView.as_view(), name='fraude_guia'),
    path('guia/relatorio/', FraudeRelatorioView.as_view(), name='fraude_relatorio'),
    path('guia/raw/', FraudeGuiaRawView.as_view(), name='fraude_guia_raw'),
]
