from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Avg, Max, Min, Count

from .models import Squirrel
from .forms import SquirrelForm


# Create your views here.

def list_sq(request):
	list_squirrels = Squirrel.objects.all()
	context = {'squirrels': list_squirrels}
	return render(request, 'sightings/list.html', context)

def edit_sq(request, squirrel_id):
	squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
	if request.method=='Post':
		form = SquirrelForm(request.POST, instance=squirrel)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/{squirrel_id}')
	else:
		form = SquirrelForm(instance=squirrel)
	context ={
		'form':form
			}
	return render(request, 'sightings/edit.html', context)

def add_sq(request):
	if request.method=='Post':
		form = SquirrelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelForm()
	context ={
		'form':form
			}
	return render(request, 'sightings/add.html', context)

def stats(request):
	squirrels = Squirrel.objects.all()
	total = len(squirrels)
	lattitude = squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
	longitude = squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
	primary_fur_color =list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
	running = list(squirrels.values_list('Running').annotate(Count('Running')))
	shift = list(squirrels.values_list('Shift').annotate(Count('Shift')))
	context = {'total': total,
		'lattitude': lattitude,
		'longitude': longitude,
		'primary_fur_color': primary_fur_color,
		'running': running,
		'shift': shift,
		}
	return render(request, 'sightings/stats.html', context)
