from django.shortcuts import render
# import string library function 
import string 
    


# Create your views here.
def home(req):

    userInput = req.GET.get('userInput')

    output = ""


    if(req.GET.get('upperCase') == 'on'):
        output = userInput.upper()
        userInput = output
    
    
    if(req.GET.get('lowerCase') == 'on'):
        output = userInput.lower()
        userInput = output
  


    if(req.GET.get('punctuation') == 'on'):
        output = ""
        for c in userInput:
            if c not in string.punctuation:
                output += c
        
                
  
    data = {
        'output': output
    }
    return render(req,'index.html',data)
