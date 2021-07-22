from re import S
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewsets, PostViewsets

router = SimpleRouter()
router.register('users', UserViewsets, basename='users')
router.register('', PostViewsets, basename='posts')



urlpatterns = router.urls