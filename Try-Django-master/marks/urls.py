from django.urls import path
from .views import (
    MarksCreateView,
    MarksDeleteView,
    MarksDetailView,
    MarksListView,
    MarksUpdateView,
)

app_name = 'marks'
urlpatterns = [
    path('', MarksListView.as_view(), name='marks-list'),
    path('create/', MarksCreateView.as_view(), name='marks-create'),
    path('<int:id>/', MarksDetailView.as_view(), name='marks-detail'),
    path('<int:id>/update/', MarksUpdateView.as_view(), name='marks-update'),
    path('<int:id>/delete/', MarksDeleteView.as_view(), name='marks-delete'),
]