from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, \
    BookmarkUpdateView, BookmarkDetailView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]

