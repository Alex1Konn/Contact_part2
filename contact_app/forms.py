from django import forms

class ContactForm(forms.Form):
    TOPICS = [
        ('question', 'Вопрос'),
        ('complaint', 'Жалоба'),
        ('suggestion', 'Предложение'),
    ]

    name = forms.CharField(label='Имя', max_length=50)
    email = forms.EmailField(label='Email')

    topic = forms.ChoiceField(label='Тема', choices=TOPICS)

    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))