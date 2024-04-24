from django import forms
from .models import CallMe

class CallForm(forms.ModelForm):
    name_form = forms.CharField(
        label='Введите имя',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите имя'}))
    tel_form = forms.CharField(
        label='Введите телефон',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'})
    )

    text_form = forms.CharField(
        label='Текст сообщения',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-text', 'placeholder': 'Введите сообщение'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CallMe
        fields = ['name_form', 'tel_form', 'text_form']
