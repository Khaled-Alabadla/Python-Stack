from django.contrib import admin
# Register your models here.
from .models import Show


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'network', 'release_date')
	search_fields = ('title', 'network')
# Register your models here.
