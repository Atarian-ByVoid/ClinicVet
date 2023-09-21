from django.urls import path

from projeto import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home_view),
    path('', views.home_view, name='home'),
    path('veterinario/', views.veterinario_view),
    path('contato/', views.contato_view),
    path('info/', views.info_view),

]
