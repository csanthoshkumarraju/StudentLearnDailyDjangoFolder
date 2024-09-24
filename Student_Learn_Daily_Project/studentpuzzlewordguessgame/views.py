from django.shortcuts import render, redirect, get_object_or_404
from studentregisterapp.models import StudentRegistrationModel
from .models import StudentPuzzleGuessGame
import random
from django.db.models import Sum

original_words = [
    "basketball", "chocolate", "firefighter", "notebooks", "snowflakes",
    "adventure", "calculator", "watermelon", "mountainous", "journalism",
    "spaghetti", "sandcastle", "wonderland", "toothbrush", "dolphin",
    "playground", "friendship", "unicorns", "celebration", "marathon",
    "photograph", "butterflies", "strawberries", "caterpillar", "blueberries",
    "chameleon", "cinnamon", "hummingbird", "icecream", "jellybeans",
    "pancakes", "stargazing", "chandelier", "heartwarming", "cloudburst",
    "rainforest", "fingernails", "bookstore", "wilderness", "drumsticks",
    "teaspoons", "homework", "lighthouse", "caterwaul", "windchimes",
    "crocodile", "skyscraper", "candlelight", "masterpiece", "caterwauling"
]

original_puzzled_words = [
    "ba__et__a__", "ch__co__ate", "fi__f__gh__r", "n__t__b__o__s", "s__o__f__kes",
    "a__e__tu__e", "c__cu__a__or", "w__e__me__o__", "m__u__ain__s", "j__r__a__m",
    "sp__g__tti", "s__d__ca__le", "w__nd__r__an", "t__th__r__sh", "d__l__hin",
    "pl__y__ou__d", "f__i__d__hip", "u__c__r__ns", "c__l__b__a__n", "m__ra__hon",
    "ph__to__ra__h", "b__tter__i__s", "st__aw__e__i__s", "c__t__rp__ll__r", "b__ue__e__ries",
    "ch__m__le__n", "c__n__m__n", "h__mm__g__ird", "i__c__r__am", "j__l__y__e__ns",
    "p__n__a__es", "s__a__g__in", "ch__nd__l__er", "h__ar__ar__ing", "c__o__d__u__t",
    "r__in__o__est", "f__n__e__ails", "b__ok__to__e", "w__l__e__ne__s", "d__u__s__icks",
    "t__as__poons", "h__m__ork", "l__g__ht__ou__e", "c__t__er__a__ul", "w__n__ch__mes",
    "c__o__o__d__ile", "s__y__cr__a__er", "c__nd__l__i__ht", "m__s__er__ie__ce", "c__t__er__a__uling"
]

def studentwordpuzleguessgame(request, student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"

    if 'puzzled_word' not in request.session:
        initialize_game(request)

    puzzled_word = request.session['puzzled_word']
    original_word = request.session['original_word']
    
    attempts = request.session.get('attempts', 0)
    message = ""
    is_correct = False

    if request.method == "POST":
        guess_word = request.POST.get('guess_word', '').strip()
        attempts += 1
        request.session['attempts'] = attempts

        if guess_word == original_word:
            message = f"It's a correct guess! The word is: {original_word}"
            is_correct = True
            request.session['correct'] = request.session.get('correct', 0) + 1
            save_game(student, request.session['attempts'], request.session['correct'])
            reset_game(request)
        else:
            message = "It's a wrong guess. Try again!"
            if attempts >= 3:
                message = f"Sorry, you've used all attempts. The word was: {original_word}"
                save_game(student, request.session['attempts'], request.session['correct'])
                reset_game(request)

    total_attempts = StudentPuzzleGuessGame.objects.filter(student=student).aggregate(Sum('total_attempts'))['total_attempts__sum'] or 0
    total_correct = StudentPuzzleGuessGame.objects.filter(student=student).aggregate(Sum('total_correct_answers'))['total_correct_answers__sum'] or 0

    return render(request, 'studentwordpuzleguessgame.html', {
        'student_id': student_id,
        'student_name': student_name,
        'puzzled_word': puzzled_word,
        'message': message,
        'is_correct': is_correct,
        'attempts': attempts,
        'total_attempts': total_attempts,
        'total_correct': total_correct,
        'success_percentage': calculate_success_percentage(student)
    })

def initialize_game(request):
    puzzled_word = random.choice(original_puzzled_words)
    puzzled_word_index = original_puzzled_words.index(puzzled_word)
    original_word = original_words[puzzled_word_index]
    request.session['puzzled_word'] = puzzled_word
    request.session['original_word'] = original_word
    request.session['attempts'] = 0
    request.session['correct'] = 0

def save_game(student, attempts, correct):
    game = StudentPuzzleGuessGame(student=student, total_attempts=attempts, total_correct_answers=correct)
    game.save()

def reset_game(request):
    del request.session['puzzled_word']
    del request.session['original_word']
    del request.session['attempts']
    del request.session['correct']

def calculate_success_percentage(student):
    total_attempts = StudentPuzzleGuessGame.objects.filter(student=student).aggregate(Sum('total_attempts'))['total_attempts__sum'] or 0
    total_correct = StudentPuzzleGuessGame.objects.filter(student=student).aggregate(Sum('total_correct_answers'))['total_correct_answers__sum'] or 0
    return (total_correct / total_attempts * 100) if total_attempts > 0 else 0
