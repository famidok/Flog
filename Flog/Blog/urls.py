from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    # path('contact/', views.contact, name='contact'),
    # path('links/', views.links, name='links'),
    # path('projects/', views.projects, name='projects'),
    path('CV/', views.CV, name='CV'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
#remove when u will publish the sit this jobs belongs to nginx
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)