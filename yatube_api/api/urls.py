from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PostViewSet, GroupViewSet, CommentViewSet


app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
