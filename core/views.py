# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from core.forms import ContactForm
from core.models import Contact


# Create your views here.
def home(request):
    return render(request, 'core/index1.html', {})

def formulario(request):
    contatos = Contact.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            novo_contato = form.save()
            return HttpResponseRedirect(reverse('url:core_forms'))
    else:
        form = ContactForm()
            

    return render(request, 'core/index.html', {
            'contatos': contatos,
            'form': form
         })
    
def detail(request, id):
    contato = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contato)
        if form.is_valid():
            novo_contato = form.save()
            return HttpResponseRedirect(reverse('url:core_forms'))
    else:
        form = ContactForm(instance=contato)
    
    return render(request, 'core/detail.html', {
        'contato': contato,
        'form': form,                                            
    })