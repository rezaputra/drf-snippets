from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls)
]







# from django.urls import path, include

# urlpatterns = [
#     path('', include('snippets.urls')),
#     path('api-auth/', include('rest_framework.urls'))
# ]