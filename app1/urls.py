from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app1.views import FinancialdataView,AnalyticsView, register_user, user_logout


router = routers.DefaultRouter()
router.register(r'Financialdata',FinancialdataView)
router.register(r'Analytics', AnalyticsView)
urlpatterns = [
    
    path('',include(router.urls)),
    #path('',register_user,name='register'),
    path('',user_logout,name='user_logout'),
    
]