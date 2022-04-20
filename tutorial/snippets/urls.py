from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippets")
router.register(r'users', views.UserViewSet, basename="users")

# The API URLs are now determined automatically by the route.
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)
