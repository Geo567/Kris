from django.urls import path
from .views import (
    SchoolboysCreateView,
    #SchoolboysDeleteView,
    #SchoolboysDetailView,
    #SchoolboysListView,
    #SchoolboysUpdateView,
    index,
)

app_name = 'schoolboys'
urlpatterns = [
   # path('', SchoolboysListView.as_view(), name='schoolboys-list'),
    path('./create/', SchoolboysCreateView.as_view(), name='schoolboys-create'),
   # path('<int:id>/', SchoolboysDetailView.as_view(), name='schoolboys-detail'),
    #path('<int:id>/update/', SchoolboysUpdateView.as_view(), name='schoolboys-update'),
    #path('<int:id>/delete/', SchoolboysDeleteView.as_view(), name='schoolboys-delete'),

]
 
urlpatterns += [
    path('', index)
   
]
