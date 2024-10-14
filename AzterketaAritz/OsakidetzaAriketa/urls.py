from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
 path('', views.zitak_list,name="zitak_list"),
 path('zitak-new/', views.zitak_new,name="zitak_new"),
 path('zitak-ezabatu/<int:id>', views.zitak_ezabatu, name='zitak_ezabatu'),
  
 path('medikuak/', views.medikuak, name='medikuak'),
 path('mediko-datuak/', views.medikuak_list, name='mediko-list'),
 path('mediko-new/', views.mediko_new, name='mediko_new'),
 path('mediko-delete/', views.mediko_delete, name='mediko_delete'), 
 path("mediko-edit/<int:medikua_id>", views.medikua_editatu, name="medikua_editatu"),
   
 path('pazienteak/', views.pazienteak, name='pazienteak'),
 path('paziente-datuak/', views.pazienteak_list, name='pazienteak-list'),
 path('paziente-new/', views.paziente_new, name='paziente_new'),
 path('paziente-delete/', views.paziente_delete, name='paziente_delete'),
 path("paziente-edit/<int:paziente_id>", views.pazientea_editatu, name="pazientea_editatu"),
 
]