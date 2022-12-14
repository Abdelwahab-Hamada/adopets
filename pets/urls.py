from django.urls import path,include

from .schema import schema

# from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from graphql_jwt.decorators import jwt_cookie


urlpatterns=[
    path("", jwt_cookie(csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True,schema=schema)))),
]