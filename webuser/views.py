from django.shortcuts import render

# Create your views here.
from .models import UserBase
from .serializers import UserBaseSerializer
from rest_framework import viewsets
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='UserBase API')
    return response.Response(generator.get_schema(request=request))

class UserBaseViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = UserBase.objects.all()
    serializer_class = UserBaseSerializer