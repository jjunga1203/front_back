from django.shortcuts import render
import random as r

# Create your views here.
def index(request):
    context = {
        'ran_num':[r.randrange(1,45), r.randrange(1,45), r.randrange(1,45), r.randrange(1,45), r.randrange(1,45), r.randrange(1,45)]

    }

    return render(request, 'pages/index.html', context)

