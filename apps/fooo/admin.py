from django.contrib import admin
from .models import Bar
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category

admin.site.register(Bar)


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, MyAdmin)
