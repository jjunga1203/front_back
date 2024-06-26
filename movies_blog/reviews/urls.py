
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.index, name='index'),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:review_pk>', views.detail, name='detail'),
    path('delete/<int:review_pk>', views.delete, name='delete'),
    path('edit/<int:review_pk>', views.edit, name='edit'),
    path('like/<int:review_id>', views.review_like, name='review_like'),
    path('create_comment/<int:pk>', views.create_comment, name='create_comment'),
    path('<int:review_id>/comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('review_like_users/<int:review_idx>', views.review_like_users, name='review_like_users'),
]

# 이미지업로드 로직을 위하여 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로 추가

