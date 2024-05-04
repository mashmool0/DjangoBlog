from django import forms


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=500, label='Enter Your Messages:')
