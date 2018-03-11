from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^comment/(?P<image_id>[0-9]+)/$', views.add_comment, name='add_comment'),
    url(r'^image/(\d+)',views.my_image,name ='single_image'),
    



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
