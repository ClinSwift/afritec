from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('root:dashboard')
        elif request.user.is_authenticated == None:
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page!')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group =='User':
            return redirect('root:UserDashboard')      
        elif group =='admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('root:login')
    return wrapper_function

def login_required(function_to_wrap):
    @wraps(function_to_wrap)
    def wrap(*args, **kwargs):
        if "some_admin_name" in session:
            return function_to_wrap(*args, **kwargs)
        else:
            flash("\"You shall not pass!\" - Gandalf")
            return redirect(url_for("login"))
    return wrap