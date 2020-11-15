from django import forms

class ProfileForm(forms.Form):
    website = forms.URLField(required=True)
    biography = forms.CharField( max_length=200, required=True)
    phone_number = forms.CharField( max_length=200, required=True)
    picture = forms.ImageField(required=False)
