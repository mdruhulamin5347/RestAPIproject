from rest_framework import serializers
from .models import contactserializer, serializerss, blogpost

class contactserializerform(serializers.ModelSerializer):
    class Meta:
        model = contactserializer
        fields = '__all__'

class contactserializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    details = serializers.CharField(max_length=60)


    def create(self, validated_data):
        return serializerss.objects.create(**validated_data)
    
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.details = validated_data.get('details', instance.details)
        instance.save()
        return instance

class postserializer(serializers.ModelSerializer):
    class Meta:
        model = blogpost
        # fields = "__all__"
        exclude = ['user',]


from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']