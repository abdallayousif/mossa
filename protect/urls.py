from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Prodect_list),
    path('<int:id>',views.Prodect_det),
]