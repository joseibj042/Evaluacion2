from django.shortcuts import render

def home_view(request):
    temas = [
        {
            'id': 1,
            'nombre': 'Python',
            'descripcion': 'Lenguaje de programación interpretado, de alto nivel y propósito general. Su filosofía enfatiza una sintaxis limpia y una gran legibilidad.',
            'imagen1': 'images/img1.png',
            'imagen2': 'images/img2.png',
        },
        {
            'id': 2,
            'nombre': 'Django',
            'descripcion': 'Framework web de alto nivel para Python que fomenta el desarrollo rápido y un diseño limpio, basado en el patrón arquitectónico MVT.',
            'imagen1': 'images/img3.png',
            'imagen2': 'images/img4.png',
        }
    ]
    return render(request, 'inicio_benavides/home.html', {'temas': temas})

def detalle_tema(request, tema_id):
    temas = {
        1: {
            'nombre': 'Python',
            'descripcion': 'Explora la versatilidad de Python a través de su sintaxis elegante, su amplio ecosistema de librerías y su potencia en áreas como desarrollo web, automatización e inteligencia artificial.',
            'imagenes': ['images/img1.png', 'images/img2.png']
        },
        2: {
            'nombre': 'Django',
            'descripcion': 'Descubre el poder de Django para construir aplicaciones web seguras, escalables y mantenibles de forma eficiente, aprovechando su potente ORM y su panel de administración integrado.',
            'imagenes': ['images/img3.png', 'images/img4.png']
        }
    }
    tema = temas.get(tema_id)
    return render(request, 'inicio_benavides/detalle.html', {'tema': tema})