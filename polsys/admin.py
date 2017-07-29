# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Evento)
admin.site.register(Bairro)
admin.site.register(TipoPenalCp)
admin.site.register(Cidade)


