from django import forms


class AboutMeForm(forms.Form):
    full_name = forms.CharField(
        label='full name',
        widget=forms.TextInput()
    )