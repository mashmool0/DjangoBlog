from django.shortcuts import render, redirect
from .forms import ContactUsForm, MessagesForm
from home.models import Messages


# Create your views here.
def contact(request):
    form = MessagesForm()
    if request.method == "POST":
        form = MessagesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get('text')
            Messages.objects.create(title=title, text=text)
            return redirect('contactus_app:contactus')
        else:
            print("chakhan")
    else:
        print("chakhan2")

    return render(request, 'account/contact.html', context={'form': form})
