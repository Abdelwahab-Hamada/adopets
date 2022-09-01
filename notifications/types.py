import graphene
from graphene_django import DjangoObjectType

from .models import Notification

class NotificationType(DjangoObjectType):
    class Meta:
        model=Notification
        fields=('id','content','sender','reciever')

    time_ago= graphene.String()

    def resolve_time_ago(self,_):
        return self.time_ago()