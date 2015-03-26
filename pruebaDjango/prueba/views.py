from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required





def myLogin(request, *args, **kwargs):
    """
    Establece el tiempo de vida de la sesion.
    request: HttpRequest con el contenido de la pagina actual.
    args: Argumentos para la funcion contrib.auth.views.login.
    kwargs: Keyword Arguments para la funcion contrib.auth.views.login.
    Retorna el resultado de la funcion contrib.auth.views.login.
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('main'))
    else:
        if request.method == 'POST':
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(604800)
        
        return login(request, *args, **kwargs)

@login_required
def main(request):
    """Vista para la plantilla main.html
    request: HttpRequest con los datos de la sesion del usuario actual.
    args: Argumentos para la funcion.
    kwargs: Keyword Arguments para la funcion.
    Template mainAdmin.html para el Administrador y mainAnyUser.html para los demas usuarios.
    """
    if request.user.is_superuser:
        return render(request, 'mainAdmin.html', {'user': request.user})
    else:
        return render(request,'inicio.html',{})
    