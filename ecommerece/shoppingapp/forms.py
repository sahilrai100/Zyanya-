from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from shoppingapp.models import completeorder
# from django_recaptcha.fields import ReCaptchaField

class registrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.IntegerField()
    
    class Meta: 
        model=User
        fields=['username','email','password1','password2','phone']
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email and not email.endswith(('in' , 'com')):
            raise forms.ValidationError("email is not verified")
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email ID already registered")
        return email
    
class login_form(forms.Form):
    username=forms.CharField(max_length=255, required=True)
    password=forms.CharField( max_length=255, required=True ,widget=forms.PasswordInput)

class forgetpass(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=255,widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if username and password and confirm_password:
            if password != confirm_password :
                raise forms.ValidationError("password does not match")
            
            if len(password)<8 or len(confirm_password)<8:
                 self.add_error('password', "Password must be at least 8 characters long")
            
            
        return cleaned_data
    
class requestotp(forms.Form):
    otp=forms.CharField(max_length=4,)
    def clean_otp(self):
        otp=self.cleaned_data.get('otp')
        if otp:
            if len(otp) !=4 :
                raise forms.ValidationError("otp must be 4 digits")
            
        return otp

class completeorderform(forms.ModelForm):
    username=forms.CharField(max_length=255,disabled=True)
    email=forms.EmailField(disabled=True)
    class Meta:
        model=completeorder
        fields="__all__"

