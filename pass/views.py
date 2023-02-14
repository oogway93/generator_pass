from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return HttpResponse("<h1>Салам</h1>")


def generator_pass(request):
    generated_password = ''

    lowercase = list('abcdefghijklmnopqrstuvwxyz')

    length_of_pass = int(request.GET.get('length', 10))

    if request.GET.get('uppercase'):
        lowercase.extends(list('ABCDEFGHIJKLMNOPQRSUVWXYZ'))
    if request.GET.get('numbers'):
        lowercase.extends(list('0123456789'))
    if request.GET.get('symbols'):
        lowercase.extends(list('!@#$%^&*'))
    if request.GET.get('hard_symbols'):
        lowercase.extends(list('~()_-+={[}]|\:;><.?/'))

    for i in range(length_of_pass):
        generated_password += random.choice(lowercase)

    return render(request, 'pass.home.html', {'gen_pass': generated_password})
