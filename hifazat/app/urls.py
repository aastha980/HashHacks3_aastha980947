from django.conf.urls import url
from . import views
app_name='app'

urlpatterns=[
  url(r'^index/$',views.index,name='index'),
  url(r'^route/$',views.route,name='route'),
  
]
