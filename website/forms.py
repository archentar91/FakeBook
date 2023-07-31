from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms 
from .models import Record

#Login Form
class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Username Required.</small></span>'
        
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = ''
        self.fields['password'].help_text = '<span class="form-text text-muted"><small>Password Required.</small></span>'
        
#Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Username Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Email Adress</small></span>'
        
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>First Name Required</small></span>'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Last Name</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

#Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Country", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")
    class Meta:
        model = Record
        exclude = ("user",)
        
    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>First Name</small></span>'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Last Name</small></span>'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Email Adress</small></span>'
        
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].label = ''
        self.fields['phone'].help_text = '<span class="form-text text-muted"><small>Phone Number</small></span>'
        
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['country'].label = ''
        self.fields['country'].help_text = '<span class="form-text text-muted"><small>Country</small></span>'
        
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['city'].label = ''
        self.fields['city'].help_text = '<span class="form-text text-muted"><small>City</small></span>'
        
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address' 
        self.fields['address'].label = ''
        self.fields['address'].help_text = '<span class="form-text text-muted"><small>Address</small></span>'
        
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['state'].label = ''
        self.fields['state'].help_text = '<span class="form-text text-muted"><small>State</small></span>'
        
        self.fields['zipcode'].widget.attrs['class'] = 'form-control'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zipcode'
        self.fields['zipcode'].label = ''
        self.fields['zipcode'].help_text = '<span class="form-text text-muted"><small>Zipcode</small></span>'
        
#Custom UpdateProfileForm
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Enter your first name.</small></span>'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Enter your first name.</small></span>'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Enter your last name.</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Enter your email address.</small></span>'

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}))

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = ''
        self.fields['old_password'].help_text = '<span class="form-text text-muted"><small>Enter your old password.</small></span>'

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data

