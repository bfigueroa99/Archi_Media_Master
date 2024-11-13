from django.shortcuts import render
from backend.models import NewsArticle  # Importa el modelo NewsArticle

def index(request):
    return render(request, 'frontend/index.html')

def article_list(request):
    articles = NewsArticle.objects.all()
    return render(request, 'frontend/article_list.html', {'articles': articles})

