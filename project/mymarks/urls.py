from django.urls import path
from .views import views(
    Authed,
)
app_name = 'mymarks'
urlpatterns = [
    path('', views.main, name='main'),
    #path('login/', views.loginp, name='loginp'),
    path('register/', views.registerp, name='registerp'),
    #path('./', views.authed, name='authed'),
    path('logout/', views.logoutp, name='logoutp'),
    path('authed/addmark/', views.addmark, name='addmark')
]
