from django.shortcuts import render

def home(request):
    data = {
        'titulo': 'Bienvenido a nuestro sitio',
        'mensaje': 'Esto es un mensaje de bienvenida',
        
    }
    return render(request, 'tienda/index.html', data)