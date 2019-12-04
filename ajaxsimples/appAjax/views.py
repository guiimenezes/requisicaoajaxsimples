from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    template_name = 'index.html'

    return render(request, template_name)

def filtroAjax(request):
    if request.method=='GET':
        nome = request.GET['nome']
        return HttpResponse(nome)
