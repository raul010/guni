# -*- coding: utf-8 -*-
from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact



## Classe antes do ModelForm

# class ContactForm(forms.Form):
#     first_name = forms.CharField(label='Nome', max_length=30)
#     last_name = forms.CharField(label='Sobrenome', max_length=30)
#     email = forms.EmailField(label='Email', max_length=75)
#     twitter = forms.URLField(label='Twitter', max_length=200)
#     
#     def save(self, contato=None):
#         nome = self.cleaned_data.get('first_name')
#         sobrenome = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#         twitter = self.cleaned_data.get('twitter')
#         
#         if contato:
#             contato.first_name = nome
#             contato.last_name = sobrenome
#             contato.email = email
#             contato.twitter = twitter
#             contato.save()
#             return contato
#         else:
#             novo_contato = Contact(
#                        first_name = nome,
#                        last_name = sobrenome,
#                        email = email,
#                        twitter = twitter,
#             )
#             
#             novo_contato.save()
#             return novo_contato
#     
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if Contact.objects.filter(email=email):
#             raise forms.ValidationError('Email já cadastrado')
#         return email
#     
# #     def clean_twitter(self):
# #         twitter = self.cleaned_data.get('twitter')
# #         if Contact.objects.filter(twitter=twitter):
# #             raise forms.ValidationError('Twitter já cadastrado')
# #         return twitter
        
        
        