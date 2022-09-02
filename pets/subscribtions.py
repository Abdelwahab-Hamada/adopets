import channels_graphql_ws
import graphene
from graphql_jwt.decorators import login_required


class Notification(channels_graphql_ws.Subscription): 
    notification_queue_limit = 64
    
    content=graphene.String()
    sender = graphene.String()

    class Arguments:
        reciever = graphene.String()

    @staticmethod
    @login_required
    def subscribe(self, info):
        reciever=info.context.user.username
        return [reciever]

    @staticmethod
    def publish(self, info):
        content=self['content']
        sender=self['sender']

        return Notification(content=content,sender=sender)