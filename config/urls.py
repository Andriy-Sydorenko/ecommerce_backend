from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("store.urls", namespace="store")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/doc/", SpectacularSwaggerView.as_view(), name="swagger"),

    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
