from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('apps.general.urls')),
    path('products/', include('apps.products.urls')),
    path('users/', include('apps.users.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('cart/', include('apps.carts.urls')),
    path('order/', include('apps.orders.urls')),
    path('comment/', include('apps.comments.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns