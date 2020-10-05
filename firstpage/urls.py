from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('signin/main/',views.main),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('admin/', admin.site.urls),
]
