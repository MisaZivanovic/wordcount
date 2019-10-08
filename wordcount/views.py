from django.http import HttpResponse
from django.shortcuts import render
import operator
def wordcounter(x):
    file1 = x

    recnik = dict()

    #for linije in file1:
        # print(linije)
        # linije.split()
    for recenice in file1.split():
        recnik[recenice] = recnik.get(recenice, 0) + 1
    najcesca_rec = None
    kolicina = None

    for rec, broj in recnik.items():

        if najcesca_rec is None or broj > kolicina:
            najcesca_rec = rec
            kolicina = broj
    return najcesca_rec.upper() + " je najcesca rec i ponavlja se " + str(kolicina) + " puta"

#x=open("new fuzz.gif","r")
def wordlista(x):

    wordlista=x.split()
    worddictionary={}
    for word in wordlista:
        if word in worddictionary:
            #Increase
            worddictionary[word] +=1
        else:
            #add to dictionary
            worddictionary[word]=1

    return sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def eggs(request):
    return HttpResponse('x')
    #x.close()

def rodjeni(request):
    return render(request, "main.html")

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    print(type(fulltext))
    wordlist=fulltext.split()
    #rec=wordcounter(fulltext)
    rec=wordlista(fulltext)
    return render (request, "count.html", {"fulltext": fulltext,'count':len(wordlist),"rec":rec })
