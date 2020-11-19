from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index1.html')

def analyze(request):

    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    lowcaps = request.POST.get('lowcaps','off')
    firstcaps = request.POST.get('firstcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    newlineremover = request.POST.get('newlineremover','off')
    countletters = request.POST.get('countletters','off')



    # analyzed = djtext
    if removepunc == "on":
        puncatuations = '''<>!~@#$%^&*()_+-=`{}[]\|?/,.''"":;'''
        analyzed = ""
        for char in djtext:
            if char not in puncatuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Uppercase Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if(lowcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.lower()
        params = {'purpose': 'Lowercase Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if(firstcaps == "on"):
        analyzed = ""
        analyzed = analyzed + djtext.capitalize()
        params = {'purpose': 'First Case ', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if(djtext[index] == "" and djtext[index]+1 == ""):
                pass
            else:
                analyzed += djtext
            params = {'purpose': 'Extra Spaces Removed ', 'analyzed_text': analyzed}
        djtext = analyzed
    if(countletters == "on"):
        analyzed = ""
        count = int(0)
        for char in djtext:
            count = int(count+1)
        analyzed += str("Number Of Characters are : " + str(count))
        params = {'purpose': 'Number of Characters ', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == "\n"):
                pass
            else:
                analyzed += djtext
            params = {'purpose': 'New Line Removed ', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc != "on" and fullcaps != "on" and lowcaps != "on" and firstcaps != "on" and extraspaceremover != "on" and countletters != "on"and newlineremover != "on"):
        return HttpResponse('''<h1 style = "text-align:center;margin-top:15rem;">Error-404</h1>''')
    return  render(request, "analyze1.html", params)



def about(request):


    return render(request, 'About.html')


def contact(request):

    contact = "Contact Us"
    return render(request, 'Contact.html')
def portfolio(request):
    return render(request,'Portfolio.html')
