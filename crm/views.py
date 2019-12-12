from django.shortcuts import render, HttpResponse

html_base = """
<h1> CRM Confival </h1>
<ul>
    <li><a href="/home/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
    <li><a href="/contacto/">Contacto</a></li>
</ul>
"""

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
    return HttpResponse(html_base + """      
        <h2> Acerca de </h2>
        <p> Sentencias y conciliaciones - inversión en activos </p>    
    """) 

def portafolio(request):
    # html_response = "<h1> CRM Confival </h1>"
    # for i in range(10):
    #     html_response += "<h2> Portada </h2>"
    return HttpResponse(html_base + """
        <h2> Portafolio </h2>
        <p> Algunos de sus trabajos </p>
    """)

def contacto(request):
    return HttpResponse(html_base + """      
  
    """)