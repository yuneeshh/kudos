from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class KudosAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"status":"Excellent", "user":str(user)})
        return Response({"status":"Excellent"})

    def post(self, request, pk=None, *args, **kwargs):
        user = request.user
        kudo_user = User.objects.filter(id=int(pk)).first()
        return Response({"status":"Excellent", "user":user})

        