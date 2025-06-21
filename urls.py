from django.urls import path

from Shopkeeper import views


urlpatterns = [
    path('login', views.login),
    path('SKRegister', views.SKRegister),
    path('RegAction', views.RegAction),
    path('LogAction', views.LogAction),
    path('SKHome', views.SKHome),
    path('addProducts', views.addProducts),
    path('ProductAction', views.ProductAction),
    path('viewproducts', views.viewproducts),
    path('viewbookings', views.viewbookings),
    path('AcceptProduct', views.AcceptProduct),




]
