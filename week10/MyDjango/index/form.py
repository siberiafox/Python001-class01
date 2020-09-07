from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type':'meail','class':'form-control','placeholder':'E-mail'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), min_length=6)
    # remember = forms.CheckboxField(widget=forms.CheckboxInput(attrs={'type':'checkbox','value':'Remember Me'}))