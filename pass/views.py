from django.shortcuts import render
from django.http import HttpResponse
import random


def generator_pass(request):
    generated_password = ''

    lowercase = list('abcdefghijklmnopqrstuvwxyz')

    length_of_pass = int(request.GET.get('length', 7))

    if request.GET.get('uppercase'):
        lowercase.extend(list('ABCDEFGHIJKLMNOPQRSUVWXYZ'))
    if request.GET.get('numbers'):
        lowercase.extend(list('0123456789'))
    if request.GET.get('symbols'):
        lowercase.extend(list('!@#$%^&*'))
    if request.GET.get('hard_symbols'):
        lowercase.extend(list('~()_-+={[}]|\:;><.?/'))

    for i in range(length_of_pass):
        generated_password += random.choice(lowercase)

    return render(request, 'pass/password.html', {'gen_pass': generated_password})


def home(request):
    return render(request, 'pass/home.html')


def about(request):
    return render(request, 'pass/about.html')
