from django.shortcuts import render

# Create your views here.
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from hangman.models import Game
from django import forms
from hangman.forms import GuessForm
from django.views.decorators.csrf import csrf_protect
import re

def index(request):
	# x = 'hippopotamus'
	# g = Game(word=x,word_length=len(x),current_state='_'*len(x))
	# g.save()
	random_word = Game.objects.get(pk=2)
	random_word.current = True
	random_word.save()
	template = loader.get_template('hangman/index.html')
	form = GuessForm()
	context = RequestContext(request, {
        'word':random_word,
        'form':form,
        'status':random_word.status
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
			current_game = Game.objects.get(current=True)
			print "wrong", current_game.wrong_guesses
			print "word", current_game.word
			print "prev guessed", current_game.guessed_letters
			
			if current_game.wrong_guesses == 10:
				current_game.status = "game over, you lose!"
			if current_game.current_state == current_game.word:
				current_game.status = "you win! now to play another game..."
				current_game.current = False
				# CHANGE THIS LOGIC TO RANDOMLY CHOOSE A NEW WORD!!!
				random_word = Game.objects.get(pk=1)
				random_word.current = True
				random_word.save()
			else:
				if new_guess in current_game.guessed_letters:
					current_game.status = "you already guessed that letter, guess again."
					current_game.save()
					return HttpResponseRedirect('/hangman/index.html', {'form': form})
				else:
					if new_guess in current_game.word:
						current_game.status = "nice, that letter was found. guess again."
						char_list = list(current_game.current_state)
						for m in re.finditer(new_guess,current_game.word):
							x = m.start()
							char_list[x] = new_guess
						current_game.current_state = "".join(char_list)
						current_game.guessed_letters = current_game.guessed_letters+new_guess
						current_game.save()
						print current_game.current_state
						return HttpResponseRedirect('/hangman/index.html', {'form': form, 'word':current_game, 'status':current_game.status})

					else:
						current_game.status = "not found, guess again"
						current_game.wrong_guesses += 1
						current_game.guessed_letters = current_game.guessed_letters+new_guess
						current_game.save()


			# reset form
			form = GuessForm()
			return HttpResponseRedirect('/hangman/index.html', {'form': form})
		else:
			form = GuessForm()
			return HttpResponseRedirect('/hangman/index.html', {'form': form})

	return render(request, 'index.html', {'form': form})