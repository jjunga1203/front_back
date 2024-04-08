from django.shortcuts import render

def save_review(request):
    data = request.GET
    print(data.get('text_name'))
    context = {
        'text_name':data.get('text_name')
    }
    return render(request, 'pages/save_review.html', context)