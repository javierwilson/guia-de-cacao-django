# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm

from solo.admin import SingletonModelAdmin
from suit_ckeditor.widgets import CKEditorWidget

from .models import Contacto, Acerca

class ContactoAdmin(SingletonModelAdmin):
    model = Contacto
    fieldsets = [
      (None, {
        'fields': ['informacion_contacto', 'contacto_general']}
      )
    ]

class AcercaAdmin(SingletonModelAdmin):
    model = Acerca
    fieldsets = [
      (None, {
        'fields': ['informacion_bienvenida']}
      )
    ]

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Acerca, AcercaAdmin)
