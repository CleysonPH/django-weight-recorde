from django.contrib import admin

from .models import Weight


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'weight_date')
