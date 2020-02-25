from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Weight
from .forms import WeightForm


@login_required
def dashboard(request):
    weight_list = Weight.objects.filter(insert_by=request.user)
    weight_chart_data = {
        'labels': [weight.weight_date.strftime('%d/%m/%Y') for weight in weight_list],
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
    if request.method == 'POST':
        form = WeightForm(request.POST)

        if form.is_valid():
            weight = form.save(commit=False)
            weight.insert_by = request.user
            weight.save()
            return redirect('weight_recorder:dashboard')

    form = WeightForm()
    context = {
        'title': 'Adicionar novo peso',
        'form': form,
    }

    return render(request, 'weight_recorder/weight_form.html', context)


@login_required
def weight_edit(request, pk):
    weight = get_object_or_404(Weight, pk=pk, insert_by=request.user)

    if request.method == 'POST':
        form = WeightForm(request.POST, instance=weight)

        if form.is_valid():
            form.save()
            return redirect('weight_recorder:dashboard')

    form = WeightForm(instance=weight)
    context = {
        'title': 'Editar peso',
        'form': form,
    }

    return render(request, 'weight_recorder/weight_form.html', context)


@login_required
def weight_delete(request, pk):
    weight = get_object_or_404(Weight, pk=pk, insert_by=request.user)
    weight.delete()
    return redirect('weight_recorder:dashboard')
