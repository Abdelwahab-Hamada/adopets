import graphene
from graphene_django import DjangoObjectType

from .models import Pet,AdoptionRequest

from django.contrib.auth.models import User


class PetType(DjangoObjectType):
    class Meta:
        model=Pet
        fields=('id','name','age','photo','owner')

    time_ago= graphene.String()

    def resolve_photo(self,info):
        return info.context.build_absolute_uri(self.photo.url)

    def resolve_time_ago(self,_):
        return self.time_ago()

class ReqType(DjangoObjectType):
    class Meta:
        model=AdoptionRequest
        fields=('id','potintialOwner','pet','created_on') 

class UserType(DjangoObjectType):
    class Meta:
        model=User
        fields=('username',)