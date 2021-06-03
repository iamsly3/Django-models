from django.http import HttpResponse

# Create your views here.

#def index(request):
    #return HttpResponse("Hello")




def index(request):
     data = { 
             
        "Name :" "Sylvester Worrell \n",

        "Track :" "Python Backend \n ",

        "Message :" "Hi Mentor, you're doing a great job! but i could really used a lil more help please. Thank you ",
     }
   


     return HttpResponse (data)