import json
import re
import bcrypt
import jwt

from my_settings import SECRET
from .models     import Account

from django.views           import View
from django.http            import HttpResponse, JsonResponse
from django.core.validators import validate_email, ValidationError


PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_])[A-Za-z\d!@#$%^&*()_]{8,}$'

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])
        
            if not re.match(PASSWORD_VALIDATION, data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 400)
            
            if not Account.objects.filter(email = data['email']).exists():
                password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
                
                Account.objects.create(
                    name     = data['name'],
                    email    = data['email'],
                    password = password,
                    address  = data['address'],
                    phone    = data['phone'],
                )
                return HttpResponse(status = 200) 
            
            return JsonResponse({'message': 'DUPLICATE_EMAIL'}, status = 400)

        except KeyError:     
            return JsonResponse({'message': 'INVALID_KEY'}, status = 400)

        except ValidationError:
            return JsonResponse({'message': 'INVALID_EMAIL'}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])

            if not re.match(PASSWORD_VALIDATION, data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 400)

            if Account.objects.filter(email = data['email']).exists():
                user = Account.objects.get(email= data['email'])
                
                if bcrypt.checkpw(data['password'].encode(), user.password.encode()):
                    token = jwt.encode({'user_id':user.id}, SECRET['secret'], algorithm = SECRET['algorithm']).decode()
                    
                    return JsonResponse({'Authorization': token}, status = 200)

            return HttpResponse(status = 401) 
        
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status = 400)
        
        except ValidationError:
            return JsonResponse({'message': 'INVALID_EMAIL'}, status = 400)