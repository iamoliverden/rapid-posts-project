# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.http import JsonResponse
from .models import Post


@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return (Response({'data': serializer.data}))
    elif request.method == 'POST':
        post = Post()
        post.text = request.data['text']
        post.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def like_post(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        setattr(post, 'likesCount', post.likesCount + 1)
        post.save()
        return Response(post.likesCount, status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_post(request, id):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'message': 'Post not found'}, status=404)
    return JsonResponse({'message': 'Invalid request method'}, status=400)
