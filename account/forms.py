from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=10, label='Enter Your Messages:')
    name = forms.CharField(max_length=10, label='Enter Your Name:')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # How to Show Error for one input or field in Forms part 2
        # if 'a' in name :
        #     raise ValidationError(message="a cant be in your name",code='a_in_name')

        if name == text:
            raise ValidationError(message="Text and Name Are same!!!", code="same_password")

    # How To show Error for one input or field in Forms part 1
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError(message="a Can't be in Your name", code="a_in_name")
        return name # inja mitony name ro taghir bedi va onni mighaye ro return kone  mishe data ro taghir dad bad return kard
