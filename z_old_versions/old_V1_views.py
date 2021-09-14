from django.shortcuts import render


def index(request):
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        test = 'User Logged Out'
    else:
        test = 'User Logged In'
        
    context = {
        'course': 'Django Framework Course Recap',
        'another_key': 'Another Value From another_key \
            inside a context object',
        'login': test
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
