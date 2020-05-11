from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='user-home'),
    path('about/',views.about,name='about'),
    path('complaint/<bill_id>',views.complaint,name='complaint'),
    path('transaction/<bill_id>/',views.transaction,name='transaction')
]
