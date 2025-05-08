from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthorsView(APIView):
    def get(self, request):
        return Response({
            "integrantes": [
                {"nombre": "Juan David Cruz Angel", "código": "329805"},
                {"nombre": "Julian  Zambrano", "código": " no lo se "}
            ]
        })
