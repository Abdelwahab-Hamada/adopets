import graphene
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required


from .types import PetType,UserType,ReqType
from .subscribtions import Notification 
from .models import Pet,AdoptionRequest

from django.contrib.auth.models import User

from notifications.models import Notification as NotificationModel

class CreatePet(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        age=graphene.Int(required=True)
        photo=Upload(required=True)
    pet=graphene.Field(PetType)

    @login_required
    def mutate(cls,info,name,age,photo):
        owner=info.context.user
        pet=Pet(
            name=name,
            age=age,
            photo=photo,
            owner=owner
        )
        pet.save()

        return CreatePet(pet=pet)

class RequestPet(graphene.Mutation):
    class Arguments:
        pet_id=graphene.String(required=True)
    request=graphene.Field(ReqType)
    created=graphene.Boolean()

    @login_required
    def mutate(cls,info,pet_id): 
        user=info.context.user
        pet=Pet.objects.get(id=pet_id)

        request=AdoptionRequest(
            potintialOwner=user,
            pet=pet
        )
        request.save()

        reciever=pet.owner
        payload={
            'content':request,
            'sender':user.username
        }

        notification=NotificationModel(
            content=request,
            sender=user,
            reciever=reciever
        )
        notification.save()

        Notification.broadcast(payload=payload,group=reciever.username)

        return RequestPet(request=request,created=True)

class Register(graphene.Mutation):
    class Arguments:
        username=graphene.String(required=True)
        password=graphene.String(required=True)
    user=graphene.Field(UserType)

    @classmethod
    def mutate(cls,root,info,username,password):
        user=User.objects.create_user(
            username=username,
            password=password)

        return Register(user=user)

class Notify(graphene.Mutation):
    sent=graphene.Boolean()

    class Arguments:
        notification = graphene.String(required=True)
        reciever = graphene.String(required=True)

    
    @classmethod
    @login_required
    def mutate(cls, _, info, notification, reciever):#for testing only
        sender=info.context.user
        if sender is None:
            return Notify(sent=False)

        payload={
            'content':notification,
            'sender':sender.username
        }

        Notification.broadcast(payload=payload,group=reciever)

        return Notify(sent=True)