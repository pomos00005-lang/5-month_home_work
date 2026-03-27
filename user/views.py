from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ConfirmCode
from random import randint
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class RegistrationAPIView(APIView):

    def post(self,req):
        username = req.data.get('username')
        password = req.data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            is_active = False
        )

        code = str(randint(100000,999999))

        ConfirmCode.objects.create(
            user=user,
            code=code
        )
        
        return Response(status=status.HTTP_201_CREATED,
                        data={'user_id':user.id,'code':code})
    

class ConfirmAuthAPIView(APIView):
    
    def post(self,req):
        user_id = req.data.get('user_id')
        user_code = req.data.get('user_code')

        try:
            confirm = ConfirmCode.objects.get(user_id=user_id)

            if confirm.code != user_code:
                return Response(data={'error':'Invalid code'},
                                       status=status.HTTP_404_NOT_FOUND)
            user = confirm.user

            user.is_active = True
            user.save()
            return Response(data={"ползователь успешно активирован!"})


        except ConfirmCode.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'error':'user not found!!!'})
            
class AuthorizationAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {'error': 'invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"token": token.key},
            status=status.HTTP_200_OK
        )