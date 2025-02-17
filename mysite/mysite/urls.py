from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
                  #path('', RedirectView.as_view(url='/recipe/', permanent=True)),
                  path('admin/', admin.site.urls),
                  path('recipe/', include('recipe.urls')),
                  path('api/', include('myAPIapp.urls')),

          ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
