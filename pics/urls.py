from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.picture_of_day, name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^pictures/(\d+)', views.filtered, name='filtered'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)