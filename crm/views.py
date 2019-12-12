from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # html_response = "<h1> CRM Confival </h1>"
    # for i in range(10):
    #     html_response += "<h2> Portada </h2>"
    # return HttpResponse(html_base + """
    #     <h2> Portada </h2>
    #     <p> Esto es la portada </p>
    # """)

    return render(request, "crm/home.html", )

def about(request):
    # return HttpResponse(html_base + """      
   
    # """) 
    return render(request, "crm/about.html")

def portafolio(request):
    return render(request, "crm/portafolio.html")   

def contacto(request):
    return render(request, "crm/contact.html")