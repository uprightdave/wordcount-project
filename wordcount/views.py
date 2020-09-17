
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

    #return render(request, 'about.html')

#def about(request)
#    return render(request, 'about.html')

#    return HttpResponse('Hello')
#     return render(request, 'home.html', {'hithere':'This is me'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
        #Increase
            worddictionary[word] += 1
        else:
        #add to dictionary
            worddictionary[word] = 1


            sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

#    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist), 'worddictionary':worddictionary.items()})
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
#    return render(request, 'count.html',{'fulltext':fulltext})
#    wordlist = fulltext.split()

#def eggs(request):
#    return HttpResponse("Eggs are great!")

#def about(request):
#    return HttpResponse("Eggs are great!")
#<a href="{% url 'home' %}">Start Again</a>
