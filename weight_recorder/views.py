from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Weight


@login_required
def dashboard(request):
    weight_list = Weight.objects.filter(insert_by=request.user)

    context = {
        'title': 'Dashboard',
        'weight_list': weight_list,
    }

    return render(request, 'weight_recorder/dashboard.html', context)
