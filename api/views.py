import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.views import View
from hashlib import sha512


class AuthView(View):

    def create_auth_token(self, email: str, password: str) -> str:
        result = sha512()
        result.update(bytes(email, "utf-8"))
        result.update(bytes(password, "utf-8"))
        return result.hexdigest()

    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            data = json.loads(request.body.decode("utf-8"))
            email = data['email']
            password = data['password']
            name = data['name']
            surname = data['surname']
            user = auth.authenticate(request, username=email, password=password)
            if user:
                auth.login(request, user)
                response = HttpResponse("authenticated")
                response.set_cookie("auth_token", self.create_auth_token(email, password))
                return response
            else:
                if User.objects.filter(username=email).exists():
                    response = HttpResponse("Already exists")
                    response.status_code = 403
                else:
                    User.objects.create(username=email, password=password, first_name=name, last_name=surname)
                    response = HttpResponse(self.create_auth_token(email, password))
                    response.set_cookie("auth_token", self.create_auth_token(email, password))
                return response
        except KeyError as e:
            print(e)
            return HttpResponse("Bad credentials", status_code=400)
