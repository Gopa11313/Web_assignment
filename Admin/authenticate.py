from django.db.models import Q
from django.shortcuts import redirect

from Admin.models import Customer, Admin


class Authenticate:

    def valid_user(function):
        def wrap(request, id):
            try:

                Customer.objects.get(Q(email=request.session['email']) & Q(
                    password=request.session['password']))
                return function(request, id)

            except:
                return redirect("/")

        return wrap

    def withoutid(function):
        def login(request):
            try:

                Customer.objects.get(Q(email=request.session['email']) & Q(
                    password=request.session['password']))
                return function(request)

            except:
                return redirect("/")

        return login

    def adminauth(function):
        def adminlogin(request):
            try:

                admin.objects.get(Q(email=request.session['email']) & Q(
                    password=request.session['password']))
                return function(request)

            except:
                return redirect("/")

        return adminlogin
