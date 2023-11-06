from django.http import HttpResponse
from .models import Producto
from django.shortcuts import redirect, render
#from .forms import UsuarioForm
#from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from .forms import RecomendacionForm
from django.contrib.auth import login, authenticate

# Create your views here.

def login(request):
    return render(request, 'login.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {
        'productos': productos
    }) 

def form_rec(request):
    if request.method == 'POST':
        form = RecomendacionForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y obtiene las respuestas
            marca = form.cleaned_data['marca']
            tipo_de_piel = form.cleaned_data['tipo_de_piel']
            problemas_piel = form.cleaned_data.get('problemas_piel', [])
            
             # Mensajes de depuración
            print(f"Marca: {marca}")
            print(f"Tipo de piel: {tipo_de_piel}")
            print(f"Problemas de piel: {problemas_piel}")

            # Lógica de recomendación de productos basada en las respuestas
            productos_recomendados = Producto.objects.filter(
                marca=marca,
                tipo_de_piel=tipo_de_piel,
                problemas_piel__in=problemas_piel
            )
            print(f"Productos recomendados: {productos_recomendados}")
            return render(request, 'prod_rec.html', {'productos': productos_recomendados})
    else:
        form = RecomendacionForm()
    
    return render(request, 'form_rec.html', {'form': form})

def productos_recomendados(request):
    marca = 'MarcaPorDefecto'
    tipo_de_piel = 'TipoDePielPorDefecto'
    problemas_piel = []
    productos_recomendados = Producto.objects.filter(
        marca=marca,
        tipo_de_piel=tipo_de_piel,
        problemas_piel__in=problemas_piel
    )
    return render(request, 'prod_rec.html', {'productos': productos_recomendados})

def registro_iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # Maneja el registro
        if 'registrarse' in request.POST:
            if form.is_valid():
                user = form.save()
                print("Usuario registrado:", user.username)
                messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
                # Autentica al usuario después del registro si lo deseas
                # ...
                return redirect('login')  # Redirige a la página de inicio de sesión

        # Maneja el inicio de sesión
        elif 'iniciar_sesion' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/website/')  # Redirige a la página de perfil o a donde desees
            else:
                # Manejar error de inicio de sesión inválido
                return render(request, 'login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos'})

    else:
        form = CustomUserCreationForm()

    return render(request, 'login.html', {'form': form})