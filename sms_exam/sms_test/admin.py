from django.contrib import admin
from .models import ChemicalElement, Commodity, EC_MAP


# Register your models here.

admin.site.register(ChemicalElement)
admin.site.register(Commodity)
admin.site.register(EC_MAP)



