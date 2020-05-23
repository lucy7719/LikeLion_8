from django.conf.urls import url
from django.contrib import admin
from youtube import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('detail/<int:detail_id>',views.detail,name='detail'),
    url(r'^admin/', admin.site.urls),
    url('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT)
