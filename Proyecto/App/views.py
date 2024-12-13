# App/views.py
from django.shortcuts import render, redirect
from .models import Producto, Reseña
from .models import Schedule, Booking
from .forms import BookingForm
from django.http import JsonResponse
from django.contrib import messages


def get_cart_data(request):
    carro = request.session.get('carro', [])
    return JsonResponse({'status': 'success', 'carro': carro})

def anadir_al_carro(request, id):
    if request.method == 'POST':
        carro_actual = request.session.get('carro', [])
        
        for producto in carro_actual:
            if producto["id_producto"] == id:
                producto["cantidad"] += 1
                request.session['carro'] = carro_actual
                return JsonResponse({'status': 'success', 'carro': serialize_carro(carro_actual)})
        
        # Fetch product details from the database
        product = Producto.objects.get(id=id)
        
        # Add product details to the cart
        carro_actual.append({
            "id_producto": id, 
            "cantidad": 1, 
            "nombre": product.nombre, 
            "precio": float(product.precio),  # Convert Decimal to float
            "imagen_url": product.imagen.url  # Include image URL
        })
        request.session['carro'] = carro_actual
        return JsonResponse({'status': 'success', 'carro': serialize_carro(carro_actual)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def reducir_del_carro(request, id):
    if request.method == 'POST':
        carro_actual = request.session.get('carro', [])
        
        for producto in carro_actual:
            if producto["id_producto"] == id:
                if producto["cantidad"] > 1:
                    producto["cantidad"] -= 1
                else:
                    carro_actual.remove(producto)
                request.session['carro'] = carro_actual
                return JsonResponse({'status': 'success', 'carro': serialize_carro(carro_actual)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def eliminar_del_carro(request, id):
    if request.method == 'POST':
        carro_actual = request.session.get('carro', [])
        
        for producto in carro_actual:
            if producto["id_producto"] == id:
                producto["cantidad"] = 0
                carro_actual.remove(producto)
                request.session['carro'] = carro_actual
                return JsonResponse({'status': 'success', 'carro': serialize_carro(carro_actual)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def aumentar_del_carro(request, id):
    if request.method == 'POST':
        carro_actual = request.session.get('carro', [])
        
        for producto in carro_actual:
            if producto["id_producto"] == id:
                producto["cantidad"] += 1
                request.session['carro'] = carro_actual
                return JsonResponse({'status': 'success', 'carro': serialize_carro(carro_actual)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def serialize_carro(carro):
    for item in carro:
        item['precio'] = float(item['precio'])
    return carro





# Vista para la página de inicio
def index(request):
    lista_productos = Producto.objects.all()
    mensaje = None if lista_productos else "No hay productos disponibles en este momento."

    if not 'carro' in request.session:
        request.session['carro'] = []
    carro_actual = request.session.get('carro', [])
    total_carro = sum(item['precio'] * item['cantidad'] for item in carro_actual)
    reseñas = Reseña.objects.all()

    return render(request, 'index.html', {
        'productos': lista_productos,
        'mensaje': mensaje,
        'carro': carro_actual,
        'total_carro': total_carro,
        'reseñas': reseñas
    })

# Vista para mostrar productos

def productos(request):
    # Recuperar todos los productos de la base de datos
    lista_productos = Producto.objects.all()  # Asegúrate de que tu modelo Producto está definido correctamente

    # Puedes agregar un mensaje o manejar el caso de que no haya productos
    mensaje = None if lista_productos else "No hay productos disponibles en este momento."

    # Recuperar el carrito actual de la sesión
    if not 'carro' in request.session:
        request.session['carro'] = []
    carro_actual = request.session.get('carro', [])
    total_carro = sum(item['precio'] * item['cantidad'] for item in carro_actual)
    reseñas = Reseña.objects.all()

    return render(request, 'productos.html', {
        'productos': lista_productos,
        'mensaje': mensaje,
        'carro': carro_actual,
        'total_carro': total_carro,
        'reseñas': reseñas
    })


# Vista para mostrar servicios
def servicios(request):
    lista_productos = Producto.objects.all()
    mensaje = None if lista_productos else "No hay productos disponibles en este momento."

    if not 'carro' in request.session:
        request.session['carro'] = []
    carro_actual = request.session.get('carro', [])
    total_carro = sum(item['precio'] * item['cantidad'] for item in carro_actual)
    reseñas = Reseña.objects.all()

    return render(request, 'servicios.html', {
        'productos': lista_productos,
        'mensaje': mensaje,
        'carro': carro_actual,
        'total_carro': total_carro,
        'reseñas': reseñas
    })
# Vista para mostrar contacto
def contacto(request):
    lista_productos = Producto.objects.all()

    mensaje = None if lista_productos else "No hay productos disponibles en este momento."

    if not 'carro' in request.session:
        request.session['carro'] = []
    carro_actual = request.session.get('carro', [])
    total_carro = sum(item['precio'] * item['cantidad'] for item in carro_actual)
    reseñas = Reseña.objects.all()

    return render(request, 'contacto.html', {
        'productos': lista_productos,
        'mensaje': mensaje,
        'carro': carro_actual,
        'total_carro': total_carro,
        'reseñas': reseñas
    })
def schedule_list(request):
    schedules = Schedule.objects.filter(available=True)
    schedule_list = []
    for schedule in schedules:
        schedule_list.append({
            'title': 'Disponible',
            'start': f'{schedule.date}T{schedule.time}',
            'url': f"{request.build_absolute_uri('/book_schedule/')}{schedule.id}/"
        })
    return JsonResponse(schedule_list, safe=False)

def schedule_page(request):
    return render(request, 'schedule_list.html')

def book_schedule(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.schedule = schedule
            booking.save()
            schedule.available = False
            schedule.save()
            messages.success(request, f'¡Hora agendada exitosamente para {booking.name} el {schedule.date} a las {schedule.time}!')
            return redirect('index')  # Redirige a la página de inicio después de reservar
    else:
        form = BookingForm(initial={'schedule': schedule})
    return render(request, 'book_schedule.html', {'form': form, 'schedule': schedule})