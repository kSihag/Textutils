from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext=request.POST.get('text','default')
    
    # Check checkbox values
    removepunc=request.POST.get('removepunc','default')
    fullcaps=request.POST.get('fullcaps','default')
    newlineremover=request.POST.get('newlineremover','default')
    extraspaceremover=request.POST.get('extraspaceremover','default')
    
   
    # Check which checkbox in on.
    if removepunc == "on":
        punctuations='''~`!@#$%^&*()_-:";'<>?/.,|\}{[]'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to uppercase','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if (newlineremover=="on"):
        analyzed = ""  
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New line remover','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index])==" " and (djtext[index+1]==" "):
                analyzed=analyzed + char
        params = {'purpose':'Extra Space removed','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(removepunc != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation !")

     


    return render(request,'analyze.html',params)


    
    
# def capfirst(request):
#     return HttpResponse("Capitalize first")

# def newlineremove(request):
#     return HttpResponse("New line remove")

# def spaceremove(request):
#     return HttpResponse("Space remove")

# def charcount(request):
#     return HttpResponse("Character Count")


