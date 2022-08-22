from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, CatReadOnlySet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cat-FULL')
router.register('cats-read', CatReadOnlySet, basename='cat-READ')
router.register('owners', OwnerViewSet, basename='owners')

urlpatterns = [
    path('', include(router.urls)),
]
