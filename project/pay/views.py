from django.shortcuts import render

def home (request):
    return render(request, "pay/index.html")

def recieve (request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        userid = request.POST.get('userid')
        password = password.POST.get('pass1')

        



    


# Create your views here.
