from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, CatReadOnlySet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cat')
router.register('cats-read', CatReadOnlySet, basename='cat-READ')

urlpatterns = [
    path('', include(router.urls)),
]