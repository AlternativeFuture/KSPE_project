from django import forms
from .models import University


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ["name", "address", "subject"]

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject.split()) < 2:
            raise forms.ValidationError('Provide min 2 subjects:')
        return subject

