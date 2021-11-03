from django.shortcuts import render
from rest_framework import status
from rest_framework import APIView
from rest_framework import Response
from rest_framework import IsAuthenticated, AllowAny
from rest_framework import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
