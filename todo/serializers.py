from rest_framework import serializers
from todo.models import *


# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=128)
#     dob = serializers.DateField()
#     email = serializers.EmailField()
#     db_folder = serializers.CharField(max_length=50)
#     dropped_out = serializers.BooleanField(default=False)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.dob = validated_data.get('dob', instance.dob)
#         instance.email = validated_data.get('email', instance.email)
#         instance.db_folder = validated_data.get('db_folder', instance.db_folder)
#         instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
#         instance.save()
#         return instance

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id','name', 'creation_date','user')

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ( 'id','completed', 'descrip', 'due_by','list')
