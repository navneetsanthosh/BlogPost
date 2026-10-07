from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import blogpost
from .serializer import Blogpostserializer,UserSerializer


# Create your views here.

class BlogPostView(APIView):
    def get(self,request):
        posts = blogpost.objects.all()
        serializer = Blogpostserializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Blogpostserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BlogPostDetail(APIView):
    def get(self,request,pk):
        posts = blogpost.objects.filter(id=pk)
        serializer = Blogpostserializer(posts,many=True)
        return Response(serializer.data)
    def put(self,request,pk):
        posts = blogpost.objects.filter(id=pk)
        serializer = Blogpostserializer(posts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        posts = blogpost.objects.filter(id=pk)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





