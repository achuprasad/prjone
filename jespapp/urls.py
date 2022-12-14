from django.urls import path
from . import views



urlpatterns = [
    path('',views.LogView.as_view(),name='demo'),
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.Login.as_view(),name='login'),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('common/',views.CommonPage.as_view(),name='common'),
    path('logout/',views.logout_view,name='logout'),
    path('documents/',views.DocumentView.as_view(),name='document')
]