from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginuser),
    path('logout',views.logoutuser),
    path('home',views.home),
    path('see/<str:cat>',views.see),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    path('mysearch',views.search, name='mysearch'),
    path('check',views.check),
    path('signup',views.signup),
]