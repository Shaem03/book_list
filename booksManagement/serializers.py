from rest_framework import serializers
from . import models
from booksManagement.models import BookLists


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'book_name', 'author','publication','summary','year_of_publication','status')
        model = BookLists