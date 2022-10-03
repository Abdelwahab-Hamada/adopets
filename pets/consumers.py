import channels_graphql_ws

from .schema import schema

class Consumer(channels_graphql_ws.GraphqlWsConsumer):
    schema = schema

    # Uncomment to send keepalive message every 42 seconds.
    # send_keepalive_every = 42

    # Uncomment to process requests sequentially (useful for tests).
    # strict_ordering = True

    async def on_connect(self, payload):
        if not self.scope['user'].is_authenticated:
            #this exception to reject nonlogged clients
            raise Exception("login first")
        print("New client connected!")
        

   
