from django.shortcuts import render

def index(request):
    context = {
        'title': 'My Website',
        'contibutor': 'Muhardiansyah',
        'nav': [
                ['/','Home'],
                ['/blog','Blog'],
                ['/about', 'About'],    
                ['/contact', 'Contact'],
            ],
        'main_background': 'img/background.png',
    }
    return render(request, 'index.html', context)
