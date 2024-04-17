from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:review_idx>', views.detail, name="detail"),
    path('update/<int:review_idx>', views.update, name="update"),
    path('delete/<int:review_idx>', views.delete, name="delete")
]

