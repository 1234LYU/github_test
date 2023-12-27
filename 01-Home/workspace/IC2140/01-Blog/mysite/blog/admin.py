from django.contrib import admin

# Register your models here.

from .models import Entry
admin.site.register(Entry)

from .models import Inventory
admin.site.register(Inventory)

from .models import Owner
admin.site.register(Owner)