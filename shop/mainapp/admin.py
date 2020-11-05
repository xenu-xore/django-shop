from django import forms
from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField

# Register your models here.


class NotebookCategoryChoiseField(forms.ModelChoiceField):
    pass


class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebook'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneCategoryChoiseField(forms.ModelChoiceField):
    pass


class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smaptphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Custumer)
