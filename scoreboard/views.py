from django.shortcuts import render, redirect
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

def new_Pull_ups(request):
    form = Pull_upsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('scoreboard_list')

    return render(request , 'add_Pull_ups.html', {'form': form})

def new_Dips(request):
    form = DipsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('scoreboard_list')

    return render(request , 'add_Dips.html', {'form': form})
