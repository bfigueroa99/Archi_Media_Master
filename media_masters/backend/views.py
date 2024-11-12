from django.http import JsonResponse
from .models import NewsArticle
import requests

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