from django.contrib import admin
from django.urls import path

from .views import CRCalculatorView, aluno_detail_view, curso_detail_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CRCalculatorView.as_view(), name='index'), 
    path('aluno/<int:aluno_id>/', aluno_detail_view, name='aluno_detail'),
    path('curso/<str:curso_cod>/', curso_detail_view, name='curso_detail'),
]