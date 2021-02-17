from django.urls import path,include

urlpatterns=[
    path('pos/',include('api.POS.urls'))
]