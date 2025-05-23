from django.contrib import admin
from django.urls import path, include  # 👈 include import korte hobe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # 👈 myapp er URL include kora holo
    path('product/', include('product.urls')),
    path('categories/', include('categories.urls')),

]
