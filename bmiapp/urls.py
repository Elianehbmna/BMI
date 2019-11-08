from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^updateProfile',views.updateProfile,name = 'updateProfile'),
    url(r'^results',views.result,name='results'),
    url(r'^new',views.new,name='new')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)