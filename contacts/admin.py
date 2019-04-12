from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name', 'contact_date')
    list_display_links = ('id', 'name', 'listing')


admin.site.register(Contact, ContactAdmin)
