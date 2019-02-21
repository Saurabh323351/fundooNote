from django.contrib import admin
from .models import Notes
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','created_time','reminder','is_archived','is_deleted','color','image','trash','is_pinned','user']

admin.site.register(Notes,NotesAdmin)