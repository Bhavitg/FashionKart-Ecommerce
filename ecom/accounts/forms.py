from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        global username
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered? We cannot find this user")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        try:
            user = User.objects.get(username=username)
        except:
            user=None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid Password")
        elif user is None:
            pass
        else:
            return password



class RegistrationFrom(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password" ,widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ["username","email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Password do not match")
        else:
            return password2

    def save(self, commit=True):
        user = super(RegistrationFrom, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        else:
            pass
        return user