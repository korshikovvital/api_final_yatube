from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
import base64
from django.core.files.base import ContentFile
from posts.models import Comment, Post, Follow, Group, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя'
            )
        new_queriset = Follow.objects.filter(user=user, following=following)
        if len(new_queriset) != 0:
            raise serializers.ValidationError(
                'Нельзя подписаться повторно'
            )

        return data
