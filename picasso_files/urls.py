from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

schema_view = get_schema_view(
    openapi.Info(
        title="Files API",
        default_version='v1',

        description="API description",
        # terms_of_service="",
        # contact=openapi.Contact(email=""),
        # license=openapi.License(name=""),
    ),
    generator_class=BothHttpAndHttpsSchemaGenerator,
    public=True,
    #permission_classes=(AllowAny,),
)

# Смена заголовка админки
admin.site.site_header = 'Администрирование пользователей и файлов'
admin.site.site_title = 'Администрирование'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/files/', include('files.urls', namespace='files')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
