from django.shortcuts import render


def main(request):
    '''
    Render the main page
    '''
    return render(request, 'main/main.html',)
def cloth(request):
    '''
    Render the about page
    '''
    return render(request, 'main/cloth.html')
def cap(request):
    '''
    Render the about page
    '''
    return render(request, 'main/cap.html')
def pants(request):
    '''
    Render the about page
    '''
    return render(request, 'main/pants.html')
def thing(request):
    '''
    Render the about page
    '''
    return render(request, 'main/thing.html')
def contact(request):
    '''
    Render the about page
    '''
    return render(request, 'main/contact.html')
def clothed(request):
    '''
    Render the clothed page
    '''
    return render(request, 'mained/clothed.html')
def caped(request):
    '''
    Render the caped page
    '''
    return render(request, 'mained/caped.html')
def pantsed(request):
    '''
    Render the pantsed page
    '''
    return render(request, 'mained/pantsed.html')
def thinged(request):
    '''
    Render the thinged page
    '''
    return render(request, 'mained/thinged.html')
def contacted(request):
    '''
    Render the contact page
    '''
    return render(request, 'mained/contacted.html')
def mained(request):
    '''
    Render the mained page
    '''
    return render(request, 'mained/mained.html')
def add(request):
    '''
    Render the add page
    '''
    return render(request, 'mained/add.html')
def login(request):
    '''
    Render the login page
    '''
    return render(request, 'login/login.html')