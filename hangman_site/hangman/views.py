from django.shortcuts import render

# Create your views here.
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from hangman.models import Game
from django import forms
from hangman.forms import GuessForm
from django.views.decorators.csrf import csrf_protect


def index(request):
	w = Game.objects.all()
	random_word = Game.objects.get(pk=1)
	word_chars = [c for c in random_word.word]
	template = loader.get_template('hangman/index.html')
	form = GuessForm()
	context = RequestContext(request, {
        'word': word_chars,
        'form':form
    })
	return HttpResponse(template.render(context))

@csrf_protect
def get_guess(request):
	if request.method == 'POST':
		form = GuessForm(request.POST)
		if form.is_valid():
			# logipc - save to database 
			print "hi"
			new_guess = request.POST.get("guess")
			# if new_guess in 
			print new_guess
			# reset form
			form = GuessForm()
			return HttpResponseRedirect('/hangman/index.html', {'form': form})
		else:
			form = GuessForm()
			return HttpResponseRedirect('/hangman/index.html', {'form': form})

	return render(request, 'index.html', {'form': form})