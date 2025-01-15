from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksserverapi.models import Book, Author, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'description')

class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'image', 'price', 'sale',  'description', 'genres')
        depth = 1

class BookView(ViewSet):

    def retrieve(self, request, pk):
        try:
            # Fetch book by primary key (pk)
            book = Book.objects.get(pk=pk)
            
            # Fetch the genres related to the book
            genres = Genre.objects.filter(bookgenres__book_id=book)
            book.genres = genres.all()
            
            # Serialize and return book details with genres
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        # Get the query parameters
        author = request.query_params.get('author', None)
        sale = request.query_params.get('sale', None)
        
        # If sale is passed in the query, convert to boolean (1/0)
        if sale == 'TRUE' or sale == 'true':
            sale = 1
        elif sale == 'FALSE' or sale == 'false':
            sale = 0
        
        try:
            books = Book.objects.all()

            # Filter by author if present in query parameters
            if author:
                books = books.filter(author=author)

            # Filter by sale status if present
            if sale is not None:
                books = books.filter(sale=sale)

            # Add genres to each book
            for book in books:
                genres = Genre.objects.filter(bookgenres__book_id=book)
                book.genres = genres.all()

            # Serialize and return the list of books with their genres
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': 'Check query'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        # Get author by ID
        try:
            author = Author.objects.get(pk=request.data["author"])
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create new book entry
        book = Book.objects.create(
            author=author,
            title=request.data["title"],
            image=request.data["image"],
            price=request.data["price"],
            sale=request.data["sale"],
            description=request.data["description"]
        )

        # Serialize and return the newly created book
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            # Fetch book by primary key (pk)
            book = Book.objects.get(pk=pk)
            
            # Update book fields with new data from the request
            author = Author.objects.get(pk=request.data["author"])  # Get author by ID
            book.author = author
            book.title = request.data["title"]
            book.image = request.data["image"]
            book.price = request.data["price"]
            book.sale = request.data["sale"]
            book.description = request.data["description"]
            
            # Save the updated book
            book.save()

            # Serialize and return the updated book
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            # Fetch book by primary key (pk)
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
