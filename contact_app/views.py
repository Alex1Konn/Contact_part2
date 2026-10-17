from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return redirect('thanks_page')
    else:
        form = ContactForm()

    return render(request, 'contact_app/contact.html', {'form': form})

def thanks_view(request):
    return render(request, 'contact_app/thanks.html')