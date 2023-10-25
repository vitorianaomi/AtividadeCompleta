from .models import Aluno
from django.forms import TextInput
import django_filters


class AlunoFilter(django_filters.FilterSet):
    nome_aluno = django_filters.CharFilter(widget=TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; heigth: 50px; margin-left: 10px; margin-right: 10px;'}), lookup_expr='icontains')

    class Meta:
        model = Aluno
        fields = ['nome_aluno', 'cidade', 'curso']
