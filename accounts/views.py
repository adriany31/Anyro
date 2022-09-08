from django.shortcuts import render

from accounts.models import Account

# Create your views here.


def registro(request):
    context ={}
    if request.method == 'POST':
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        username = request.POST['username']
        email = request.POST['email']
    
        #Validacion campos
        ok = True
        if not email:
         context['alarma'] = 'Ingrese el correo electronico'
         ok = False
        if not password or len(password) < 5:
         context['alarma'] = 'Ingrese un password de cinco (5) o más caracteres'
         ok = False  
        if password != confirmPassword:
         context['alarma'] = '¡El password no coincide!'
         ok = False
         
        #Todo ok
        if ok:
            existe = Account.objects.filter(email=email).exists()
            if not existe:
                user = Account.objects.create_user(first_name=username, last_name=username, username=username, email=email, password=password)
                user.save()
                context['alarma'] = 'Usuario guardado con exito!'
            else:
                context['alarma'] = '¡El correo ya existe!'
                
    return render(request, 'registro.html', context);

