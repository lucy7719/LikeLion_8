from django.contrib import admin
from django.urls import path
from youtube import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('create/',views.create,name="create"),
    path('new/',views.new,name="new"),
    path('detail/<int:detail_id>',views.detail,name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

