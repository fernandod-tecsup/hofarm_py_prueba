from django import forms

class FormSucrusal(forms.Form):

    title = forms.CharField(
        label = "Titulo"
    )