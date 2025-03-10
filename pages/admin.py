from django.contrib import admin

from . import models
from common.admin import MyTranslationAdmin


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email', 'message',)
    list_filter = ('email',)


@admin.register(models.AboutModel)
class AboutModelAdmin(MyTranslationAdmin):
    list_display = ('name', 'job')
    search_fields = ('name', 'job')
    list_filter = ('job',)