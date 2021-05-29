from django.shortcuts import render

# Create your views here.
def hello(request):
    
    return render(request, 'hello.html')

def what(request):
    sentence=request.GET['sentence']
    
    wordList =sentence.split()
    wordDict={}

    for word in wordList:
        if word in wordDict:
             wordDict[word] +=1
             print('어서오세요. 로그인하는 사자들의', {{word}},'님!')
        else:
            wordDict[word]=1
    return render(request, 'what.html',{'fulltext':sentence,'count':len(wordList), 'wordDict':wordDict.items})