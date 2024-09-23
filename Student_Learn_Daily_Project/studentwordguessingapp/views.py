# from django.shortcuts import render,get_object_or_404,redirect
# from studentregisterapp.models import StudentRegistrationModel
# # Create your views here.


# def studentwordgame(request,student_id):
#     student = get_object_or_404(StudentRegistrationModel, id=student_id)
#     student_name = f"{student.first_name} {student.last_name}"

#     return render(request,'studentwordguessinggame.html',{
#         'student_id':student_id,
#         'student_name':student_name
#     })

from django.shortcuts import render, get_object_or_404, redirect
import random
from .forms import WordGuessForm
from studentregisterapp.models import StudentRegistrationModel

def studentwordgame(request, student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"

    word_list = ["Apple", "Banana", "Cake", "Door", "Elephant", "Flower", "Guitar", "House", "Ice Cream", "Kite"]

    if f'attempts_{student_id}' not in request.session:
        request.session[f'attempts_{student_id}'] = 3
        request.session[f'word_to_guess_{student_id}'] = random.choice(word_list)
        request.session[f'result_message_{student_id}'] = ''
        request.session[f'score_{student_id}'] = 0

    form = WordGuessForm(request.POST or None)

    if request.method == 'POST':
        if 'reset' in request.POST:
            request.session.flush()
            return redirect('studentwordgame', student_id=student_id)

        if form.is_valid():
            guess = form.cleaned_data['word_game']
            word_to_guess = request.session.get(f'word_to_guess_{student_id}')
            attempts = request.session.get(f'attempts_{student_id}')

            if word_to_guess is None:
                word_to_guess = random.choice(word_list)

            if guess.lower() == word_to_guess.lower():
                request.session[f'result_message_{student_id}'] = 'Correct! You guessed the word!'
                request.session[f'score_{student_id}'] += 1
                request.session[f'word_to_guess_{student_id}'] = random.choice(word_list)
                request.session[f'attempts_{student_id}'] = 3
            else:
                attempts -= 1
                request.session[f'attempts_{student_id}'] = attempts
                
                if attempts > 0:
                    request.session[f'result_message_{student_id}'] = f'Wrong guess! You have {attempts} attempts left.'
                else:
                    request.session[f'result_message_{student_id}'] = f'Game over! The word was {word_to_guess}.'
                    request.session[f'attempts_{student_id}'] = 0

    context = {
        'student_id': student_id,
        'student_name': student_name,
        'attempts_left': request.session.get(f'attempts_{student_id}', 0),
        'result_message': request.session.get(f'result_message_{student_id}', ''),
        'score': request.session.get(f'score_{student_id}', 0),
        'form': form,
        'result_class': 'correct' if 'Correct!' in request.session.get(f'result_message_{student_id}', '') else 'wrong'
    }

    return render(request, 'studentwordguessinggame.html', context)
