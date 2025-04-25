from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Profile

CustomUser = get_user_model()


class LoginForm(forms.Form):
    user_id = forms.CharField(label="Username")
    secret_key = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('user_id')
        password = self.cleaned_data.get('secret_key')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                existing_user = CustomUser.objects.filter(username=username)
                if not existing_user:
                    raise forms.ValidationError("User not found.")
                if not existing_user[0].check_password(password):
                    raise forms.ValidationError("Invalid password.")
                if not existing_user[0].is_active:
                    raise forms.ValidationError("Account inactive. Please complete verification.")
        return super().clean()


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    company = forms.CharField(label="Organization Name")
    email = forms.EmailField(label="Primary Email")
    confirm_email = forms.EmailField(label="Re-enter Email")
    password = forms.CharField(label="Set Password", widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('1', 'Student'), ('2', 'Instructor')))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'confirm_email', 'password']

    def clean(self):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email != confirm_email:
            raise forms.ValidationError("Email entries do not match.")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return super().clean()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pro_pic', 'contact_number']
