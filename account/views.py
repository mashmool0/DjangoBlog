from django.shortcuts import render, redirect
from .forms import ContactUsForm


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['text'])
            return redirect('contactus_app:contactus')

    form = ContactUsForm()
    return render(request, 'account/contact.html', context={'form': form})
