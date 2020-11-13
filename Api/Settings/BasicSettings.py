from django.contrib import admin
from django.urls import path
# importing Views
from posts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # (Link , views.VIEWNAME.as_view())
    path('api/posts/', views.PostList.as_view()),
]
