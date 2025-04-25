from django.db import models
from Accounts.models import Examinee, Examiner
from ExamManagement.models import Exam

class ExamResult(models.Model):
    participant = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    test = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    score = models.FloatField(default=0.0, null=True)
    submission_file = models.FileField(upload_to='exam/submissions', null=True, blank=True)

    def __str__(self):
        return f"{self.participant.user.username} | {self.test.exam_title} | Score: {self.score}"

class LeaderboardEntry(models.Model):
    participant = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    test = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    score = models.FloatField(default=0.0)
    duration = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.participant.user.username} - {self.test.exam_title} - {self.score}"

class ParticipationLog(models.Model):
    participant = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    test = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    attempt_date = models.DateField()
    score = models.FloatField(default=0.0)
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()

    def __str__(self):
        return f"{self.participant.user.username} attempted {self.test.exam_title} on {self.attempt_date} - Score: {self.score}"
