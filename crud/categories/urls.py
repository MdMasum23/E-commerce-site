from django.urls import path
from .views import (
    category_list, category_create, category_update, category_delete,
    tag_list, tag_create, tag_update, tag_delete
)

urlpatterns = [
    # Category URLs
    path("categories/", category_list, name="category_list"),
    path("categories/create/", category_create, name="category_create"),
    path("categories/update/<int:pk>/", category_update, name="category_update"),
    path("categories/delete/<int:pk>/", category_delete, name="category_delete"),

    # Tag URLs
    path("tags/", tag_list, name="tag_list"),
    path("tags/create/", tag_create, name="tag_create"),
    path("tags/update/<int:pk>/", tag_update, name="tag_update"),
    path("tags/delete/<int:pk>/", tag_delete, name="tag_delete"),
]