
from django.http import HttpResponse

from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def analize(request):
    # Get the text
    doit = request.GET.get('thismydata', 'default')
    trueORfalse2 = request.GET.get(
        'trueORfalse', 'off')
    capson = request.GET.get('capson', 'off')
    charlower = request.GET.get('charlower', 'off')
    newlineremover = request.GET.get(' newlineremover', 'off')
    if trueORfalse2 == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in doit:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analize.html', params)

    elif capson == "on":
        analyzed = ""
        for char in doit:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'captilize forms is ',
                      'analyzed_text': analyzed}
            if capson == "default":
                return HttpResponse('Error')
        return render(request, 'analize.html', params)

    elif charlower == "on":
        analyzed = ""
        for char in doit:
            analyzed = analyzed + char.lower()
            params = {'purpose': 'captilize forms is ',
                      'analyzed_text': analyzed}
            if charlower == "default":
                return HttpResponse('Error')
        return render(request, 'analize.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for index, char in enumerate(doit):
            if not(doit[index] == " " and doit[index+1] == " "):
                analyzed = analyzed + char
                analyzed = analyzed+char
                params = {'purpose': 'Removed NewLines',
                          'analyzed_text': analyzed}
                if newlineremover == "default":
                    return HttpResponse('i am facing some issues..')
        return render(request, 'analyze.html', params)

    else:

        return HttpResponse('Error')
