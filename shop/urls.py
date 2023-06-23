from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),                                                                              #specific categoryilek povaanulla urls
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='detail_page'),                                                 #imgagil press cheyumbol detail pagilek povaan
    path('search',views.searching,name='search'),
    # path('base',views.base,name='base'),

]