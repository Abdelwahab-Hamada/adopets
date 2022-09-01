import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from .models import Pet
from .types import PetType
from .mutations import CreatePet,Register,Notify,RequestPet
from .subscribtions import Notification

from notifications.types import NotificationType

class Query(graphene.ObjectType):
    pets=graphene.List(PetType)
    owner_pets=graphene.List(PetType)
    notifications=graphene.List(NotificationType)

    def resolve_pets(root,info):
        return Pet.objects.all()

    def resolve_owner_pets(root,info):
        owner=info.context.user
        return owner.pets.all()
    
    def resolve_notifications(root,info):
        user=info.context.user
        return user.recieved_notifs.all()

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()

    create_pet=CreatePet.Field()
    register=Register.Field()
    # notify=Notify.Field()
    req_pet=RequestPet.Field()

class Subscribtion(graphene.ObjectType):
    subscribe_notifications=Notification.Field()

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscribtion,
)
