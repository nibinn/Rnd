from django.urls import path, re_path
from app import views
from django.conf.urls import url
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    re_path(r'^add_customer/$',views.add_customer,name='add_customer'),
    re_path(r'^show_customer/$',views.show_customer,name='show_customer'),
    re_path(r'^foc/$',views.foc_calculation,name='foc'),
    re_path(r'^predictFOC/$',views.foc_prediction,name='predictFOC'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
    
