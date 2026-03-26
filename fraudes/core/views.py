from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from .models import Licitacao
from .serializers import LicitacaoSerializer

class LicitacaoViewSet(ModelViewSet):
    queryset = Licitacao.objects.all()
    serializer_class = LicitacaoSerializer

class FraudeGuiaView(TemplateView):
    template_name = 'fraude_licitacoes.html'

class FraudeGuiaRawView(TemplateView):
    template_name = 'fraude_licitacoes_raw.html'

class FraudeRelatorioView(TemplateView):
    template_name = 'guia_relatorio.html'

class HomeView(TemplateView):
    template_name = 'index.html'
