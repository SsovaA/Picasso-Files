from django.urls import path
from .views import *

app_name = 'files'
urlpatterns = [
    path('files/', FilesAPIView.as_view()),
    path('files/<int:pk>/', OneFileAPIView.as_view()),
    path('paginated_files/', PaginatedFilesAPIView.as_view()),
    path('upload/', UploadAPIView.as_view()),
]
