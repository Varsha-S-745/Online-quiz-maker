from django.db import models

from Accounts.models import Examinee, Examiner
from ExamManagement.models import Exam


class Result(models.Model):
    examinee_user = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam_details = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    score = models.FloatField(null=True, default=0)
    file_attachment = models.FileField(null=True, blank=True, upload_to='exam/results')

    def __str__(self):
        return f"{self.examinee_user.user.username} {self.exam_details.exam_title} {str(self.score)}"


class Rank(models.Model):
    examinee_user = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam_details = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    score = models.FloatField(null=False, default=0)
    completion_time = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f"{self.examinee_user.user.username} {self.exam_details.exam_title} {str(self.score)}"


class ExamineeHistory(models.Model):
    examinee_user = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam_details = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    date_taken = models.DateField(null=False)
    score = models.FloatField(null=False, default=0)
    correct_answers = models.IntegerField(null=False)
    incorrect_answers = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.examinee_user.user.username} {self.exam_details.exam_title} {str(self.score)}"
