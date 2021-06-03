from django.shortcuts import render


def Homepage(request):

    context={
        'user' : request.user
    }
    print(context.get('user'))
    return render(request, 'home.html', context)