from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PersonForm

def person_view(request):
    result = None
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            result = f"Привет, {name}! Тебе {age} лет."
            form = PersonForm() #очищаем форму после успешной очистки
    else:
        form = PersonForm()
    return render(request, "person.html", {"form": form, "result": result})

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#
#         if form.is_valid():
#             return redirect('thanks_page')
#     else:
#         form = ContactForm()
#
#     return render(request, 'contact_app/contact.html', {'form': form})
#
# def thanks_view(request):
#     return render(request, 'contact_app/thanks.html')