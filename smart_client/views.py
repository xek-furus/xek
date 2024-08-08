from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import *
from django.contrib.auth import logout


from django.shortcuts import render

def home(request):
    """ Rend la page d'accueil client """
    return render(request, 'smart_client/index1.html')
