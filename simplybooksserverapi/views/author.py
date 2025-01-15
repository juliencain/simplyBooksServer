from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksserverapi.models import Author, Book
from django.db.models import Count

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 'last_name', 'image', 'favorite')  
        depth = 1

class SingleAuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(default=None)

    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 'last_name', 'image', 'favorite', 'book_count', 'books')  # Remove 'uid'
        depth = 1


class AuthorView(ViewSet):
    def retrieve(self, request, pk):
        try:
            # Fetch author by primary key (pk)
            author = Author.objects.get(pk=pk)

            # Count the number of books associated with the author
            book_count = Book.objects.filter(author=author).count()
            author.book_count = book_count

            # Serialize the author with book count
            serializer = SingleAuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        # Fetch all authors
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Create a new author from the provided data
        author = Author.objects.create(
            email=request.data["email"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            image=request.data["image"],
            favorite=request.data["favorite"]
        )

        # Serialize and return the created author
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            # Fetch the author by primary key (pk)
            author = Author.objects.get(pk=pk)

            # Update the author fields with the provided data
            author.email = request.data["email"]
            author.first_name = request.data["first_name"]
            author.last_name = request.data["last_name"]
            author.image = request.data["image"]
            author.favorite = request.data["favorite"]

            # Save the updated author
            author.save()

            # Serialize the updated author
            serializer = AuthorSerializer(author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            # Fetch the author by primary key (pk)
            author = Author.objects.get(pk=pk)

            # Delete the author
            author.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
