from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Weight
from .forms import WeightForm


@login_required
def dashboard(request):
    weight_list = Weight.objects.filter(insert_by=request.user)
    weight_chart_data = {
        'labels': [weight.weight_date.strftime('%m/%d/%Y') for weight in weight_list],
        'data': [weight.weight_value for weight in weight_list]
    }

    print(weight_chart_data)

    context = {
        'title': 'Dashboard',
        'weight_list': weight_list,
        'weight_chart_data': weight_chart_data,
    }

    return render(request, 'weight_recorder/dashboard.html', context)


@login_required
def weight_create(request):
    form = WeightForm()
    context = {
        'title': 'Adicionar novo peso',
        'form': form,
    }

    return render(request, 'weight_recorder/weight_form.html', context)
