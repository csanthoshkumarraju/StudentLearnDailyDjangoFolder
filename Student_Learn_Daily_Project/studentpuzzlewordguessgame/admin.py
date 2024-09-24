from django.contrib import admin
from .models import StudentPuzzleGuessGame

class StudentPuzzleGuessGameAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_attempts', 'total_correct_answers', 'success_percentage', 'last_played')
    search_fields = ('student__username',)

admin.site.register(StudentPuzzleGuessGame, StudentPuzzleGuessGameAdmin)

