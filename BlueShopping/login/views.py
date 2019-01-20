from django.shortcuts import render, render_to_response
from django.contrib import auth


def main(request):
    '''
    Render the main page
    '''
    return render(request, 'main/main.html',)

def login(request):
    '''
    Render the login page
    '''
    return render(request, 'login/login.html')
def mained(request):
    '''
    Render the mained page
    '''
    return render(request, 'mained/mained.html')




