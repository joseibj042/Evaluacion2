from django.shortcuts import render

def home_view(request):
    temas = [
        {
            'id': 1,
            'nombre': 'Python',
            'descripcion': 'Lenguaje de programación de alto nivel interpretado.',
            'imagen1': 'images/tema1_img1.jpg',
            'imagen2': 'images/tema1_img2.jpg',
        },
        {
            'id': 2,
            'nombre': 'Django',
            'descripcion': 'Framework web para Python enfocado en desarrollo rápido.',
            'imagen1': 'images/tema2_img1.jpg',
            'imagen2': 'images/tema2_img2.jpg',
        }
    ]
    return render(request, 'inicio_benavides/home.html', {'temas': temas})

def detalle_tema(request, tema_id):
    temas = {
        1: {
            'nombre': 'Python',
            'descripcion': 'Detalles avanzados sobre Python.',
            'imagenes': ['images/tema1_img1.jpg', 'images/tema1_img2.jpg']
        },
        2: {
            'nombre': 'Django',
            'descripcion': 'Detalles avanzados sobre Django.',
            'imagenes': ['images/tema2_img1.jpg', 'images/tema2_img2.jpg']
        }
    }
    tema = temas.get(tema_id)
    return render(request, 'inicio_benavides/detalle.html', {'tema': tema})