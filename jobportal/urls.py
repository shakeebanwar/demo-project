from django.contrib import admin
from django.urls import path,include



#for images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminpannel/', admin.site.urls),
    path('admin/', include('Admin.urls')),
    path('recruiter/', include('recruiter.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
