from django.urls import path
from .views import product_create, product_list, product_update, product_delete

urlpatterns = [
    path("", product_list, name="product_list"),
    path("create/", product_create, name="product_create"),
    path("update/<int:pk>/", product_update, name="product_update"),
    path("delete/<int:pk>/", product_delete, name="product_delete"),
]