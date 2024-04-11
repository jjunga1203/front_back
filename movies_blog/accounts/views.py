from django.shortcuts import render

# Create your views here.
def login(request):
    content = {

    }
    return render(request, 'accounts/login.html', content)

def login_submit(request):
    data = request.GET
    print(data)
    content = {
        'login_id': data.get('login_id'),
        'login_pw': data.get('login_pw'),
    }
    return render(request, 'accounts/login_submit.html', content)
