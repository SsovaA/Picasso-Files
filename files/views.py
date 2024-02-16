from .serializers import *
from .paginations import *
from .tasks import file_process_task
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, JSONParser

class FilesAPIView(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description='Получить список файлов',
        responses={200: FileSerializer(many=True)} 
    )
    def get(self, request):
        
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OneFileAPIView(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description='Получить один файл по id',
        responses={200: FileSerializer(many=False)} 
    )
    def get(self, request, pk):
        
        files = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(files, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PaginatedFilesAPIView(APIView, PaginationHandlerMixin):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)
    pagination_class = LimitPagination

    @swagger_auto_schema(
        operation_description='Получить список файлов с пагинацией',
        responses={200: FileSerializer(many=True)} 
    )
    def get(self, request):
        files = File.objects.all()

        page = self.paginate_queryset(files)
        if page is not None:
            serializer = self.get_paginated_response(FileSerializer(page, many=True).data)
        else:
            serializer = FileSerializer(files, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
class UploadAPIView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description='Загрузить файл',
        request_body=UploadSerializer,
        responses={201: FileSerializer(many=False)} 
    )
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            file_serializer = FileSerializer(file)
            file_process_task.delay(file.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

