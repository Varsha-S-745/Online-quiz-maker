
### 1. Create Exam Page (for Examiner)

from django.shortcuts import render, redirect
from .models import Exam
from .forms import ExamForm
from django.contrib.auth.decorators import login_required

@login_required
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.examiner = request.user.examiner  # assuming examiner is a related object
            exam.save()
            return redirect('dashboard')  # Or redirect to exam list
    else:
        form = ExamForm()
    return render(request, 'exam/create_exam.html', {'form': form})


# Forms (in forms.py):

from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam_code', 'exam_title', 'exam_marks', 'exam_date_time', 'exam_duration', 'exam_question']


# 2. Join Exam (Examinee)

from django.contrib import messages
from .models import Exam, AttemptedExam

@login_required
def join_exam(request):
    if request.method == 'POST':
        exam_code = request.POST.get('exam_code')
        try:
            exam = Exam.objects.get(exam_code=exam_code)
            if exam.isRunning():
                AttemptedExam.objects.get_or_create(exam=exam, examinee=request.user.examinee)
                return redirect('exam_detail', exam_id=exam.id)
            else:
                messages.error(request, "Exam is not running.")
        except Exam.DoesNotExist:
            messages.error(request, "Exam with that code does not exist.")
    return render(request, 'exam/join_exam.html')

admin.site.register(MCQQuestion)
admin.site.register(CustomQuestion)
`
