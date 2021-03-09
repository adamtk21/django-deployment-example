from django.conf.urls import url
from . import views

## template tagging
app_name = 'fourth_app'

urlpatterns = [
    url(r'relative/$',views.relative,name='relative'),
    url(r'other/$',views.other,name='other'),
]
