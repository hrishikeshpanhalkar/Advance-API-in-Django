from rest_framework import serializers
from .models import TODO, TimingTodo
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = TODO
        fields = ['user', 'todo_title', 'slug', 'todo_description', 'is_done', 'uid']
        # exclude = ['create_at', 'updated_at']

    def get_slug(self, obj):
        return slugify(obj.todo_title)

    def validate_todo_title(self, data):
        if data:
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(data) is None:
                raise serializers.ValidationError("todo_title cannot contains special characters!!")

        return data

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        exclude = ['create_at', 'updated_at']
        # depth = 1