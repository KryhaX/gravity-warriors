from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dips , Pull_ups
from .forms import DipsForm, Pull_upsForm


from django.db.models import F, Window
from django.db.models.functions import RowNumber

def home(request):
    return render(request, 'home.html')

def scoreboard_list(request):
    dips = Dips.objects.all().order_by('weight').reverse()
    pull_ups = Pull_ups.objects.all().order_by('weight').reverse()

    ranked_dips = [(index + 1, dip) for index, dip in enumerate(dips)]
    ranked_pull_ups = [(index + 1, pull_ups) for index, pull_ups in enumerate(pull_ups)]

    return render(request, 'scoreboard.html', {'dips': dips, 'pull_ups': pull_ups,
                                               'ranked_dips': ranked_dips, 'ranked_pull_ups': ranked_pull_ups })

@login_required
def new_Pull_ups(request):
    form = Pull_upsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('scoreboard_list')

    return render(request , 'Pull_ups_form.html', {'form': form})

@login_required
def new_Dips(request):
    form = DipsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('scoreboard_list')

    return render(request , 'Dips_form.html', {'form': form})

@login_required
def edit_Dips(request, dip_id):

    dip = get_object_or_404(Dips, pk=dip_id)

    form = DipsForm(request.POST or None, instance=dip )

    if form.is_valid():
        form.save()
        return redirect('scoreboard_list')

    return render(request, 'Dips_form.html', {'form': form, 'dip_id':dip_id})

@login_required
def edit_Pull_ups(request, pullups_id):
    pullups = get_object_or_404(Pull_ups, pk=pullups_id)

    form = Pull_upsForm(request.POST or None, instance=pullups)

    if form.is_valid():
        form.save()
        return redirect('scoreboard_list')

    return render(request, 'Pull_ups_form.html', {'form': form,'pullups_id':pullups_id})

@login_required
def delete_Dips(request, dip_id):

    dip = get_object_or_404(Dips, pk=dip_id)

    if request.method == 'POST':
        dip.delete()
        return redirect('scoreboard_list')

    return render(request, 'Delete_dip.html', {'dip': dip})

@login_required
def delete_Pull_ups(request, pullups_id):
    pullup = get_object_or_404(Pull_ups, pk=pullups_id)

    if request.method == 'POST':
        pullup.delete()
        return redirect('scoreboard_list')

    return render(request, 'Delete_pullup.html', {'pullup': pullup})
