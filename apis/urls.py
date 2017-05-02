from django.conf.urls import url, include
from apis import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = routers.DefaultRouter()
# router = DefaultRouter()
router.register(r'apis', views.ApiViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]