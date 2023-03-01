from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls',namespace = 'accounts')),
    path("admin/", admin.site.urls),
    path('', include('home.urls',namespace = 'home')),
    path('consulat/', include('consulat.urls',namespace = 'consulat'),),
    path('about/', include('about.urls',namespace = 'about')),
    path('blog/', include('blog.urls',namespace='blog')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)