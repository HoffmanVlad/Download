from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import CustomUser, Watch, Phone
from .forms import CustomUserForm, WatchForm, PhoneForm

#TemplateViewSets
class TemplateViewSet(ListView):
    template_name = 'base.html'
    model = Watch
    queryset = Watch.objects.all()


class WatchesViewSet(ListView):
    template_name = 'watches.html'
    model = Watch
    queryset = Watch.objects.all()

class AboutViewSet(ListView):
    template_name = 'about.html'

    def get_queryset(self):
        ...

class ContactViewSet(ListView):
    template_name = 'contact.html'

    def get_queryset(self):
        ...

class PhoneViewSet(ListView):
    template_name = 'phone.html'
    model = Phone
    queryset = Phone.objects.all()

class CategoryViewSet(ListView):
    template_name = 'category.html'

    def get_queryset(self):
        ...

class LaptopViewSet(ListView):
    template_name = 'laptop.html'

    def get_queryset(self):
        ...

class IpodViewSet(ListView):
    template_name = 'ipod.html'

    def get_queryset(self):
        ...

class PCViewSet(ListView):
    template_name = 'PC.html'

    def get_queryset(self):
        ...

class HeadphonesViewSet(ListView):
    template_name = 'headphones.html'

    def get_queryset(self):
        ...
##############################

#Login and Register and Logout

class LoginingView(LoginView):
    success_url = reverse_lazy('templateviewset')
    template_name = 'login.html'

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        return super().form_valid(form=form)

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    success_url = '/login/'
    template_name = 'register_page.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)


class Logout(LogoutView):
    next_page = '/'

################################

#CreatedProduct

class CreateProduct(CreateView):
    model = Watch
    form_class = WatchForm
    success_url = reverse_lazy('templateviewset')
    template_name = 'create_product.html'

class CreatePhone(CreateView):
    model = Phone
    form_class = PhoneForm
    success_url = reverse_lazy('templateviewset')
    template_name = 'create_phone.html'

###############################

    