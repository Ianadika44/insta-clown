from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/profile/$',views.profile,name = 'profile'),
    url(r'^profile/(\d+)',views.other_profile,name = 'visitprofile'),
    url(r'^search/', views.search_results, name='search_results')
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)