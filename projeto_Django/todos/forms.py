# todos/forms.py
from django import forms
from .models import Todo


# 1. Defina a classe TodoForm que herda de forms.ModelForm
class TodoForm(forms.ModelForm):
    # 2. Defina o campo deadline com os widgets/input_formats
    deadline = forms.fields.DateField(
        widget=forms.TextInput(attrs={"type": "text"}),
        input_formats=["%d%m%Y", "%d/%m/%Y", "%Y-%m-%d"],
    )

    class Meta:
        model = Todo
        fields = ["title", "deadline"]
