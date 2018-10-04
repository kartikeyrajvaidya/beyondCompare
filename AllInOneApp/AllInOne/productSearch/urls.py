from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'productSearch'

urlpatterns =[

    path('',views.SearchProduct,name='productSearch'),
    path('<productId>/',views.ProductDetail,name='productDetail'),
    path('<productId>/specs',views.ProductSpecs,name='productSpecs')
]
