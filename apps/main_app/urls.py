from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "dashboard"),
    url(r'^logout$', views.logout, name = "logout"),
    url(r'^makeplans$', views.makeplans, name = "makeplans"),
    url(r'^plans$', views.plans, name = "plans"),
    url(r'^join$', views.join, name = "join"),
    url(r'^success/(?P<number>\d+)$', views.success, name="success"),    
]