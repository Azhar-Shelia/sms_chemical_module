from django.contrib import admin
from .models import ChemicalElement, Commodity, User, Dob, EC_MAP


# Register your models here.

admin.site.register(ChemicalElement)
admin.site.register(Commodity)
admin.site.register(EC_MAP)
admin.site.register(Dob)
admin.site.register(User)



