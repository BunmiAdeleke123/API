
from django.urls import path,include
from .views import article, register, download
urlpatterns = [
    path('api/',article ),
    path('register/',register ),
    path('download/', download),

]