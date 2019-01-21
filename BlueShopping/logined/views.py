from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from account.forms import UserForm
from django.contrib.auth import logout as auth_logout

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
def register(request):
    '''
    Register a new user
    '''
    template = 'accountr/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm()})

    # POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm})

    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('mained:mained')
def logining(request):
    '''
    Login an existing user
    '''
    template = 'account/logining.html'
    if request.method == 'GET':
        return render(request, template)

    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)

    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)

    # login success
    auth_login(request, user)
    messages.success(request, '登入成功')
    return redirect('mained:mained')
def logout(request):
    '''
    Logout the user
    '''
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('main:main')