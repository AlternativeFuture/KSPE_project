from django import forms
from .models import University


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ["name", "address", "subject"]

    def subject_validator(self):
        data = self.cleaned_data.get("subject")
        if len(data.split()) < 2:
            raise forms.ValidationError("Provide min 2 subjects:")
        return data

    # def subject_validator(self):
    #     res = False
    #     if len(self.data["subject"].split()) > 1:
    #         res = True
    #     else:
    #         raise forms.ValidationError("Provide min 2 subjects:")
    # #self.errors["subject"] = "Provide minimum 2 subjects:"
    #     return res
    #
    # def is_valid(self):
    #     valid = super(UniversityForm, self).is_valid()
    #     subject_validator = self.subject_validator()
    #     if valid and subject_validator:
    #         return True
    #     else:
    #         return False
