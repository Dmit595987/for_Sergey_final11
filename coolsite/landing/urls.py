from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('reviews/', reviews, name='reviews'),
    path('contact/', contact, name='contact'),
    path('work/', work, name='work'),
    path('secret_master/', secret_master,  name='secret_master'),
    path('thanks/', thanks,  name='thanks'),
    path('work-single/', work_single,  name='work_single'),
    path('blog-single/', blog_single,  name='blog_single'),
    path('blog/', blog,  name='blog'),
]