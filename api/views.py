import json
from hashlib import sha512

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views import View

from api.models import Comment


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


class CommentsView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        comments = Comment.objects.all().order_by('date')
        return HttpResponse(json.dumps(list(
            map(lambda comment: {"author": comment.author, "contents": comment.contents, "date": str(comment.date)},
                comments))))

    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            data = json.loads(request.body.decode("utf-8"))
            author = data['author']
            contents = data['contents']
            comment, created = Comment.objects.get_or_create(author=author, contents=contents)
            if created:
                return HttpResponse("Created")
            else:
                return HttpResponse("Already exists", status=400)
        except Exception:
            return HttpResponse("Bad entity", status=422)
