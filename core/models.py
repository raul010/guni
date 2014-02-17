# -*- coding: utf-8 -*-
from django.db import models

class Contact(models.Model):
    first_name = models.CharField('Nome',
                                  blank=True,
                                  max_length=30)
    last_name = models.CharField('Sobrenome',
                                  blank=True,
                                 max_length=30)
    email = models.EmailField('Email',
                              max_length=75)
    twitter = models.URLField('Twitter',
                              max_length=200)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name. self.last_name)