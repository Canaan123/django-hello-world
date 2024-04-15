# 测试接口 get请求
# your_app/views.py
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Hello, World!"})
