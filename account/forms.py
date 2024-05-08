from django import forms
from django.core.validators import ValidationError
from home.models import Article, Messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=10, label='Enter Your Messages:', required=False)
    name = forms.CharField(max_length=10, label='Enter Your Name:', required=True)

    # birth_year = forms.DateField(label="Enter Your Birthday Date",required=True,widg)

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # How to Show Error for one input or field in Forms part 2
        # if 'a' in name :
        #     raise ValidationError(message="a cant be in your name",code='a_in_name')

        if name == text:
            raise ValidationError(message="Text and Name Are same!!!", code="same_password")

    # How To show Error for one input or field in Forms part 1
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError(message="a Can't be in Your name", code="a_in_name")
    #     return name # inja mitony name ro taghir bedi va onni mighaye ro return kone  mishe data ro taghir
    #     dad bad return kard


# class MessagesForm(forms.Form):
#     title = forms.CharField(max_length=10X`0)
#     text = forms.CharField(widget=forms.Textarea)
#     email = forms.EmailField()

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('title', 'text', 'email',)
        # fields = '__all__'

        # Set Css for fields
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Your Title",

            })
        }


class AuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'password')
    #
    #     widgets = {
    #         "username":forms.CharField(att),
    #     }

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('username')
        else:
            return ValidationError("username or Passoword are wrong", code='login_error')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
