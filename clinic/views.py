from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def veterinario_view(request):
    return render(request, 'veterinario.html')


def contato_view(request):
    return render(request, 'contato.html')


def info_view(request):
    return render(request, 'info.html')
