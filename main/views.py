from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Save
from django.shortcuts import get_object_or_404, render
from .forms import Algoritm
from django.utils import timezone


"""def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render((request)))

"""
def index(request):
    return render(request, 'main/index.html')

def aes(request):	
	if request.method == "POST":
		form = Algoritm(request.POST)
		if form.is_valid():
			key = form.cleaned_data['key']
			text = form.cleaned_data['text']
			algoritm = form.cleaned_data['algoritm']
			# implementar algoritmo
			print(key, text, algoritm)
			men = "mensaje"
			
			result = {
				'key': key,
				'text': text,
				'algoritm': algoritm,
				'men': men
			}
			s = Save(text_plain=text, cipher_text=men, algoritm=1, date=timezone.now())
			s.save()
			return render(request, 'main/result.html', result)

	form = Algoritm()
	return render(request, 'main/aes.html', {'form': form})

def eoa(request):	
	if request.method == "POST":
		form = Algoritm(request.POST)
		if form.is_valid():
			key = form.cleaned_data['key']
			text = form.cleaned_data['text']
			algoritm = form.cleaned_data['algoritm']
			#implementar algoritmo
			print(key, text, algoritm)
			men = "mensaje"
			
			result = {
				'key': key,
				'text': text,
				'algoritm': algoritm,
				'men': men
			}
			s = Save(text_plain=text, cipher_text=men, algoritm=1, date=timezone.now())
			s.save()
			return render(request, 'main/result.html', result)

	form = Algoritm()
	return render(request, 'main/eoa.html', {'form': form})



def detail (request, save_id):
	return HttpResponse('estas viendo el registro numero %s' % save_id)
