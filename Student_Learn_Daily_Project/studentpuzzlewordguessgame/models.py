from django.db import models
from studentregisterapp.models import StudentRegistrationModel

class StudentPuzzleGuessGame(models.Model):
    student = models.ForeignKey(StudentRegistrationModel, on_delete=models.CASCADE, null=True)
    total_attempts = models.IntegerField(default=0)
    total_correct_answers = models.IntegerField(default=0)
    success_percentage = models.FloatField(default=0.0)
    last_played = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.student.first_name} - Total Attempts: {self.total_attempts}, Correct Answers: {self.total_correct_answers}"

