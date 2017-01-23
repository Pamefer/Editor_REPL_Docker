from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext, loader
from django.shortcuts import render
from aplicacion.models import *
import smtplib
from aplicacion.forms import *
from django.contrib import auth as au
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.utils.decorators import method_decorator

# Create your views here.

def homeuser(request):
    usuario_actual = request.user
    return render(request, 'homeuser.html', {'usuario_actual': usuario_actual})



def compila(request):
    usuario_id = request.user
    print usuario_id
    print "sssssssssss"
    ctx = {}
    if request.method == 'POST':
        form = CodigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(compila)
    else:
        form = CodigoForm()
    ctx['form'] = form
    return render(request,'compila.html', ctx)

#3
# def compila(request):
#     us= request.user
#     print "sssssssssss"
#     ctx = {}
#     if request.method == 'POST':
#         form = CodigoForm(request.POST)
#         if form.is_valid():
#             a=Codigo.objects.get(id_usuario=us)
#             instance = CodigoForm.save(commit=False)
#             instance.id_usuario = a
#             instance.save()
#             return redirect(compila)
#     else:
#         form = CodigoForm()
#     ctx['form'] = form
#     return render(request,'compila.html', ctx)

# Permisos: Acesso si no esta logeado
def login(request):
    if request.user.is_authenticated():  # Si el usuario ya esta logueado, no hay sentido mostrarle el logeo
        return redirect(compila)
    else:
        if request.method == 'POST':
            form = FormLogin(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    return redirect(homeuser)
        else:
            form = FormLogin()
        return render(request, "home.html", {'form': form})

#Valeeeeeeeeeeeeeeeeee
# def compila(request):
#     #and request.user.is_authenticated()
#
#     if request.method == 'POST' and request.user.is_authenticated():
#         form = CodigoForm(request.POST)
#         #id_usuario = User.objects.get(id=request.user)
#         id=au.get_user(request)
#         if form.is_valid():
#                enlace=form.cleaned_data['enlace']
#                codigodes=form.cleaned_data['codigodes']
#                a=Codigo()
#                a.id_usuario= id
#                a.enlace=enlace
#                a.codigodes=codigodes
#                a.save()
#         form=CodigoForm()
#         ctx={'form':form}
#         return render(request,'compila.html', ctx)
#     else:
#         form = CodigoForm()
#         ctx = {'form': form}
#         return render(request,'compila.html', ctx)


class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return render(request, 'home.html')



from django.views.generic import TemplateView
#2
# def compila(request):
#         us=request.user
#         ctx = {}
#         formulario = ''
#         if request.method == 'POST':
#             codform = CodigoForm(request.POST, request.FILES, instance=us, prefix='us')
#             form = CodigoForm(request.POST)
#             if form.is_valid():
#                 # form.enlace = form.cleaned_data["enlace"]
#                 # form.codigodes = form.cleaned_data["codigodes"]
#                 # form.id_usuario_id = form.cleaned_data["id_usuario_id"]
#                # user = User.objects.get(id_usuario=us)
#                 tempo=CodigoForm.save(commit=False)
#                 tempo.id_usuario = codform.save()
#                 tempo.save()
#
#                 return redirect(compila)
#         else:
#             form = CodigoForm(instance=us, prefix='us')
#             ctx['form'] = form
#             return render(request, "compila.html", {'form': form})

