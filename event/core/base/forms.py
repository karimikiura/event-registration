from django.forms import ModelForm

from .models import Submission

class ProjectSubmissionForm(ModelForm):

    class Meta:
        model = Submission
        fields = ['detail']