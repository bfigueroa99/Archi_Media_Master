from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import NewsArticle
import requests
from ai_service_content.ai_service import generate_content

def handle_player_decision(request):
    if request.method == 'POST':
        decision = request.POST.get('decision')
        article_id = request.POST.get('article_id')
        article = NewsArticle.objects.get(id=article_id)
        is_correct = article.is_true == (decision == 'true')
        feedback = get_feedback(article, is_correct)
        return JsonResponse({'is_correct': is_correct, 'feedback': feedback})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_feedback(article, is_correct):
    if is_correct:
        return f'Correct! The news article "{article.title}" is true.'
    else:
        return f'Incorrect. The news article "{article.title}" is actually true.'

def generate_article_feedback(article_id):
    article = NewsArticle.objects.get(id=article_id)
    
    # Publish the article content to the AI component
    ai_response = requests.post('/ai/generate_feedback', data={
        'title': article.title,
        'content': article.content
    })
    
    if ai_response.ok:
        feedback = ai_response.json()['feedback']
        return feedback
    else:
        return 'Error generating feedback'

def article_list(request):
    articles = NewsArticle.objects.all()
    return render(request, 'frontend/article_list.html', {'articles': articles})

def generate_article_content(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    generated_content = generate_content(article.title, article.content)
    if generated_content:
        return JsonResponse({'generated_content': generated_content})
    else:
        return JsonResponse({'error': 'Failed to generate content'}, status=500)