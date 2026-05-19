from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def HomeView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('message')

    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})


def MessageView(request):
    contacts = Contact.objects.all()

    return render(request, 'message.html', {'contacts': contacts})