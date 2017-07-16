# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'blogapp/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blogapp/post_detail.html",{'post':post})
