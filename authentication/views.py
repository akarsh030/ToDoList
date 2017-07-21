# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import Account
from django.http import JsonResponse
from django.shortcuts import Http404

class logout(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self,request):
        response = HttpResponseRedirect('/accounts/login/')
        response.delete_cookie('JWT')
        response.delete_cookie('user')
        return response

def akarsh(request):
    return render_to_response('loginf.html')

from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response==None:
        return response

    if((response.status_code == 401) | (response.status_code == 403)):
        return redirect('/accounts/login/')
    else:
        return response

class RestrictedView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'id': request.user.id,
            'username': request.user.username,
            'token': str(request.auth)
        }
        return Response(data)

class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class updateprofile(APIView):
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def get_object(self,request, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        if request.is_ajax():
            aka = self.get_object(request,pk)
            serializer = AccountSerializer(aka)
            return JsonResponse(serializer.data,safe=False)
        else:
            return redirect("/accounts/login/")

    def put(self, request, pk):
        if request.is_ajax():
            ala = self.get_object(request,pk)
            serializer = AccountSerializer(ala, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return redirect("/accounts/login/")

def red(request):
    return redirect('/accounts/login/')
