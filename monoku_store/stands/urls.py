from rest_framework.routers import DefaultRouter
from django.urls import path, include

from stands import views

# Router to register views
router = DefaultRouter()
router.register(r'stands', views.StandViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'characteristics', views.CharacteristicViewSet)
router.register(r'orders', views.OrderViewSet)

#router.register(r'users', views.UserViewSet)

# The API URLs determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))

]
