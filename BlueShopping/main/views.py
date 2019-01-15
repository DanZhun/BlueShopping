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