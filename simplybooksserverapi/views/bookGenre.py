from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksserverapi.models import BookGenre, Book, Genre


class BookGenreView(ViewSet):
  
   

    def retrieve(self, request, pk):
        try:
            bookGenre = BookGenre.objects.get(pk=pk)
            serializer = BookGenreSerializer(bookGenre)
            return Response(serializer.data)
        except BookGenre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        try:
            bookGenres = BookGenre.objects.all()
            serializer = BookGenreSerializer(bookGenres, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        try:
            bookId = Book.objects.get(pk=request.data["book"])
            genreId = Genre.objects.get(pk=request.data["genre"])

            
            bookGenre = BookGenre.objects.create(
                book_id=bookId.id,  
                genre_id=genreId.id  
            )

            serializer = BookGenreSerializer(bookGenre)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Genre.DoesNotExist:
            return Response({'message': 'Genre not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        try:
            bookId = Book.objects.get(pk=request.data["book"])
            genreId = Genre.objects.get(pk=request.data["genre"])

            
            bookGenre = BookGenre.objects.get(pk=pk)

            
            bookGenre.book_id = bookId.id  
            bookGenre.genre_id = genreId.id  

            # Save the updated BookGenre
            bookGenre.save()

            serializer = BookGenreSerializer(bookGenre)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Genre.DoesNotExist:
            return Response({'message': 'Genre not found'}, status=status.HTTP_400_BAD_REQUEST)
        except BookGenre.DoesNotExist:
            return Response({'message': 'BookGenre not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        try:
            bookGenre = BookGenre.objects.get(pk=pk)
            bookGenre.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except BookGenre.DoesNotExist:
            return Response({'message': 'BookGenre not found'}, status=status.HTTP_404_NOT_FOUND)


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ('id', 'book', 'genre')
        depth = 1
