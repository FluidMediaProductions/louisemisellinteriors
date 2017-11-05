import math
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def index(request):
    fabrics = Fabric.objects.all()
    return render(request, 'curtain/index.html', {
        "fabrics": fabrics
    })


@login_required
def add(request):
    if request.method == "GET":
        form = FabricForm()
        return render(request, 'curtain/add.html', {
            "form": form
        })
    elif request.method == "POST":
        form = FabricForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('fabrics'))
        return render(request, 'curtain/add.html', {
            "form": form
        })


@login_required
def delete(request, id):
    fabric = get_object_or_404(Fabric, id=id)
    fabric.delete()
    return redirect(resolve_url('fabrics'))


@login_required
def estimate(request, id):
    fabric = get_object_or_404(Fabric, id=id)
    if request.method == "GET":
        return render(request, 'curtain/estimate.html', {
            "fabric": fabric
        })
    elif request.method == "POST":
        try:
            pole_length = int(request.POST['pole_length'])
            fullness = Decimal(request.POST['fullness'])
            drop = int(request.POST['drop'])
        except ValueError:
            return render(request, 'curtain/estimate.html', {
                "fabric": fabric
            })
        virt_pole_length = pole_length * fullness
        num_width = int(math.ceil(virt_pole_length / fabric.width))
        num_height = int(math.ceil(drop / fabric.repeat))
        per_strip = num_height * fabric.repeat
        total_length = per_strip * num_width
        total_length = (Decimal(total_length) * Decimal('1.10'))/100
        total_cost = total_length * Decimal(fabric.price)
        return render(request, 'curtain/estimated.html', {
            "fabric": fabric,
            "data": {
                "total_length": total_length,
                "total_cost": total_cost
            }
        })
