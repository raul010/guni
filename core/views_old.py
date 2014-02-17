from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from core.models import Contact
from core.forms import ContactForm
# -*- coding: utf-8 -*-

# Create your views here.
def home(request):
    return render(request, 'core/index1.html', {})

def formulario(request):
    contatos = Contact.objects.all()
    
    if request.method == 'POST':
        nome = request.POST.get('first_name')
        sobrenome = request.POST.get('last_name')
        email = request.POST.get('email')
        twitter = request.POST.get('twitter')
        novo_contato = Contact(
               first_name=nome,
               last_name=sobrenome, 
               email=email, 
               twitter=twitter
        )
        novo_contato.save()
        print('antes')
        return HttpResponseRedirect(reverse('url:core_formis'))
    
    print('depois')
    return render(request, 'core/index.html', {
            'contatos' : contatos,
         })