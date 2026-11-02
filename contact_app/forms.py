from django import forms

# class ContactForm(forms.Form):
#     TOPICS = [
#         ('question', 'Вопрос'),
#         ('complaint', 'Жалоба'),
#         ('suggestion', 'Предложение'),
#     ]
#
#     name = forms.CharField(label='Имя', max_length=50)
#     email = forms.EmailField(label='Email')
#
#     topic = forms.ChoiceField(label='Тема', choices=TOPICS)
#
#     message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

class PersonForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': "Напримерб  Анна"})
    )

    age = forms.IntegerField(
        label="Возраст",
        min_value=1,
        max_value=120,
    )

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Имя должно ссотоять только из букы")
        return name.capitalize()

