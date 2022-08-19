from django.shortcuts import render
from datetime import date
from django.contrib.auth.models import User

from .cbrf import ValueCourse

value_course = ValueCourse()


def home(request):
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        user = None

    return render(request, 'course_value/index.html', {'user':user})


def values(request):

    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        user = None

    today = str(date.today())

    values_usd = round(float(value_course.value['usd'][today]), 2)
    values_eur = round(float(value_course.value['eur'][today]), 2)
    values_cny = round(float(value_course.value['cny'][today])/10, 2)


    value = {
        'values_usd' : values_usd,
        'values_eur' : values_eur,
        'values_cny' : values_cny,
        'user' : user,
    }

    return render(request, 'course_value/value.html', value)


def author(request):
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        user = None

    return render(request, 'course_value/author.html', {'user':user})


def article(request):
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        user = None
    return render(request, 'course_value/article.html', {'user':user})
