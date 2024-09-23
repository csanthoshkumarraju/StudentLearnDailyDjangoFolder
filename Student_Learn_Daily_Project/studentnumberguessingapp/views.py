from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel 
import random
from .forms import NumberGuessForm
# Create your views here.

def studentnumberguessing(request, student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"

    # Initialize session variables for this specific student if not set
    if f'attempts_{student_id}' not in request.session:
        request.session[f'attempts_{student_id}'] = 3
        request.session[f'number_to_guess_{student_id}'] = random.randint(1, 10)
        request.session[f'result_message_{student_id}'] = ''
        request.session[f'score_{student_id}'] = 0

    form = NumberGuessForm(request.POST or None)

    if request.method == 'POST':
        if 'reset' in request.POST:
            # Reset the session variables for a new game
            request.session.flush()  # Clear all session data for this user
            return redirect('studentnumberguessing', student_id=student_id)  # Redirect to the same view

        if form.is_valid():
            guess = form.cleaned_data['number_game']
            number_to_guess = request.session[f'number_to_guess_{student_id}']
            attempts = request.session[f'attempts_{student_id}']

            if guess == number_to_guess:
                request.session[f'result_message_{student_id}'] = 'Correct! You guessed the number!'
                request.session[f'score_{student_id}'] += 1  # Increase score
                request.session[f'number_to_guess_{student_id}'] = random.randint(1, 10)  # New number
                request.session[f'attempts_{student_id}'] = 3  # Reset attempts
            else:
                attempts -= 1
                request.session[f'attempts_{student_id}'] = attempts
                
                if attempts > 0:
                    request.session[f'result_message_{student_id}'] = f'Wrong guess! You have {attempts} attempts left.'
                else:
                    request.session[f'result_message_{student_id}'] = f'Game over! The number was {number_to_guess}.'
                    request.session[f'attempts_{student_id}'] = 0  # End game

    # Prepare context data
    context = {
        'student_id': student_id,
        'student_name': student_name,
        'attempts_left': request.session.get(f'attempts_{student_id}', 0),
        'result_message': request.session.get(f'result_message_{student_id}', ''),
        'score': request.session.get(f'score_{student_id}', 0),
        'form': form,
        'result_class': 'correct' if 'Correct!' in request.session.get(f'result_message_{student_id}', '') else 'wrong'
    }

    return render(request, 'studentnumberguess.html', context)