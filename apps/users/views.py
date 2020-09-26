from django.shortcuts import render

from django.http import JsonResponse


def Index(req):
    return JsonResponse({'position': 'users/index'})

def Demo(req):
    return JsonResponse({'test1':'a0.a32s4d2fa654sd65'})