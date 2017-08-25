from django.contrib import admin
from . models import Event, Profile, Ticket

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'venue', 'event_time')
    list_filter = ('created', 'event_time', 'venue')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['created']

admin.site.register(Event, EventAdmin)


admin.site.register(Profile)
admin.site.register(Ticket)