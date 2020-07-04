import jwt

from .models     import Account
from my_settings import SECRET

from django.http import HttpResponse
from django.http import JsonResponse

def requirelogin(func):
    def wrapper(self, request, *args, **kwargs):     
        try:
            token = request.headers.get('Authorization', None)
            user_id = jwt.decode(token, SECRET['secret'], algorithm=SECRET['algorithm']).get('user_id', None)
            
            if Account.objects.filter(id = user_id).exists():
                user = Account.objects.get(id = user_id)
                request.user = user

        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status = 403)

        except Account.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status = 401)

        return func(self, request, *args, **kwargs)
    return wrapper

def check_login(func):
    def wrapper(self, request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        
        if token: 
            try:
                user_id = jwt.decode(
                    token, 
                    SECRET['secret'], 
                    algorithm = SECRET['algorithm']
                ).get('user_id', None)

                if Account.objects.filter(id = user_id).exists():
                    user = Account.objects.get(id = user_id)
                    request.user = user 
                else:
                    return HttpResponse(status = 401)

            except jwt.DecodeError:
                return JsonResponse({'message': 'INVALID_TOKEN'}, status = 403)

            except User.DoesNotExist:
                return JsonResponse({'message': 'INVALID_USER'}, status = 401)
        else:
            request.user = None

        return func(self, request, *args, **kwargs)
        
    return wrapper