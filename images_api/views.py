from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from images_api.models import Item
from images_api.serializers import ItemSerializer

from rest_framework import authentication
from .models import Item

from rest_framework import permissions

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ItemViewSet(viewsets.ModelViewSet):
    # authentication_classes = [ authentication.TokenAuthentication  , authentication.SessionAuthentication , authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsAuthenticated , IsAdminUser]

    def post(self, request, *args, **kwargs):
        file = request.data['image']
        image = Item.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


