from django.shortcuts import render

def registered(request):
    '''
    Render the register page
    '''
    return render(request, 'register/register.html') 
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
