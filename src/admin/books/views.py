from rest_framework import viewsets
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ViewSet):
    def list(self, request): #/api/books
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def create(self, request): #/api/books
        pass

    def retrieve(self, request, pk=None): #/api/books/<str:id>
        pass

    def update(self, request, pk=None): #/api/books/<str:id>
        pass

    def destroy(self, request, pk=None): #/api/books/<str:id>
        pass
