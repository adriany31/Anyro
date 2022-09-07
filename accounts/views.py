from django.shortcuts import render

from accounts.models import Account

# Create your views here.


def registro(request):
    context ={}
    if request.method == 'POST':
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        nombreUsuario = request.POST['username']
        email = request.POST['correo']
    
        #Validacion campos
        ok = True
        if not email:
         context['alarma'] = 'Ingrese el correo electronico'
         ok = False
        if not password or len(password) < 5:
         context['alarma'] = 'Ingrese un password de cinco (5) o mas caracteres'
         ok = False  
        if password != confirmPassword:
         context['alarma'] = '¡El password no coincide!'
         ok = False
         
        #Todo ok
        if ok:
            existe = Account.object.filter(email=email).exists()
            if not existe:
                user = Account.objects.create_user(first_name=nombreUsuario, last_name=nombreUsuario, username=nombreUsuario, email=email, password=password)
                user.save()
                context['alarma'] = 'Usuario guardado con exito!'
            else:
                context['alarma'] = '¡El correo ya existe!'
                
    return render(request, 'registro.html', context);

