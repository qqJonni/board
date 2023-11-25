from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def ceiling(request):
    return render(request, 'ceiling.html')


def defence(request):
    return render(request, 'defence.html')
