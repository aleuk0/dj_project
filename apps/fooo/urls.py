from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My API')

urlpatterns = [
    path("", schema_view),
    # path("", views.interface, name="interface"),
    path("interface/", views.interface, name="interface"),
    path("new_item/", views.new_item, name="new_item"),
    path("del_item/", views.del_item, name="del_item"),
    path("genres/", views.show_genres, name="genres"),
]
