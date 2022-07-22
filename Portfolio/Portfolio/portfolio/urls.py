from pipes import Template
from django.urls import path as url
from .views import CreatePhone, TemplateViewSet, WatchesViewSet, AboutViewSet,  \
ContactViewSet, UserCreateView, LoginingView, Logout, CreateProduct, \
PhoneViewSet, CategoryViewSet, LaptopViewSet, IpodViewSet, HeadphonesViewSet, PCViewSet, \
CreatePhone

urlpatterns = [
    url('', TemplateViewSet.as_view(), name="templateviewset"),
    url('timups/category/watches', WatchesViewSet.as_view(), name="watchesviewset"),
    url('timups/category/phone', PhoneViewSet.as_view(), name="phoneviewset"),
    url('timups/category/laptop', LaptopViewSet.as_view(), name="laptopviewset"),
    url('timups/category/ipod', IpodViewSet.as_view(), name="ipodviewset"),
    url('timups/category/pc', PCViewSet.as_view(), name="PCviewset"),
    url('timups/category/headphones', HeadphonesViewSet.as_view(), name="headphonsviewset"),
    url('timups/about', AboutViewSet.as_view(), name="aboutviewset"),
    url('timups/category', CategoryViewSet.as_view(), name="categoryviewset"),
    url('timups/contact', ContactViewSet.as_view(), name="contactviewset"),
    url('register/', UserCreateView.as_view(), name='register'),
    url('login/', LoginingView.as_view(), name='login'),
    url('logout/', Logout.as_view(), name='logout'),
    url('timups/create/watch', CreateProduct.as_view(), name='watches'),
    url('timups/create/phone', CreatePhone.as_view(), name='phones'),
]