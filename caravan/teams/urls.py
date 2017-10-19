from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from teams import views

urlpatterns = [
    url(r'^teams/$', views.team_list),
    url(r'^teams/(?P<pk>[0-9]+)/S', views.team_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)