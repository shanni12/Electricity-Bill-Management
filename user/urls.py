from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns=[
    path('',views.home,name='user-home'),
    path('about/',views.about,name='about'),
    path('complaint/<bill_id>',views.complaint,name='complaint'),
    path('transaction/<bill_id>/',views.transaction,name='transaction'),
    path('view-complaints/',views.view_complaints,name='view-complaints'),
    url(r'^password/$', views.change_password, name='change_password'),

]
