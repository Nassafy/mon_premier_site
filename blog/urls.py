from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^launch$',views.launch_server, name='lancement_serveur'),
    url(r'code/$', views.get_code, name='/code/ '),
    ]
