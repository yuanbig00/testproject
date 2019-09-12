from django.conf.urls import url,include
from .views import IndexView
from . import views
urlpatterns = [
 url(r'^$',IndexView.as_view(template_name='index.html'),name='index'),
 url(r'^event/(?P<ids>[0-9]+)$',views.event,name='event')
]
app_name='showchart'