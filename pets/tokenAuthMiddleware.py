from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings

@database_sync_to_async
def get_user(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware:
    def __init__(self, app):
        self.app=app

    async def __call__(self, scope, receive, send):
        token=None
        try:
            cookies=scope['headers'][10][1].decode("utf8").split(';')
            for cookie in cookies:
                if "JWT=" in cookie:
                    token=(cookie.split('=')[1])
                    # print(token)
                    # UntypedToken(token)
        except (InvalidToken, TokenError) as error:
            return None
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            scope['user'] = await get_user(decoded_data['username'])

        return await self.app(scope, receive, send) 

              
