from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ColorScheme
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    schemes = ColorScheme.objects.all()
    return render(request, 'palit/index.html', {'schemes': schemes})

@csrf_exempt
def save_scheme(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        scheme, created = ColorScheme.objects.update_or_create(
            name=data['name'],
            defaults={
                'background': data['background'],
                'menu': data['menu'],
                'menu_text': data['menu_text'],
                'text': data['text'],
                'header': data.get('header', '#222222'),
                'sidebar': data.get('sidebar', '#3a4f59'),
                'card': data.get('card', '#ffffff'),
                'footer': data.get('footer', '#444444'),
            }
        )
        return JsonResponse({'status': 'saved', 'id': scheme.id})

def get_scheme(request, scheme_id):
    scheme = get_object_or_404(ColorScheme, pk=scheme_id)
    return JsonResponse({
        'name': scheme.name,
        'background': scheme.background,
        'menu': scheme.menu,
        'menu_text': scheme.menu_text,
        'text': scheme.text,
        'header': scheme.header,
        'sidebar': scheme.sidebar,
        'card': scheme.card,
        'footer': scheme.footer,
    })