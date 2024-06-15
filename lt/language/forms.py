from .models import signup,login,feedbackt,audio,quotesg,superuser,superuserlogin
from django import forms
from django.core import validators
import re
from captcha.fields import CaptchaField

class signupform(forms.ModelForm):
    class Meta:
        model = signup
        fields = ["username", "email", "dob", "password"]
        widgets = {
                  "username": forms.TextInput(
                    attrs={
                            "class": "form-control my-2",
                            "placeholder": "user name",
                            "id": "username",
                            }
                    ),
                  "email": forms.EmailInput(
                    attrs={
                            "class": "form-control my-2",
                            "placeholder": "eg@gmail.com",
                            "id": "email",
                            "required": "True",
                            }
                    ),
                  "dob": forms.DateInput(
                    attrs={
                           "class": "form-control my-2",
                           "placeholder": "dd/mm/yyyy",
                           "id": "dob",
                           "type": "date",
                           }
                    ),
                  "password": forms.PasswordInput(
                    attrs={
                           "class": "form-control my-2",
                           "placeholder": "password",
                           "id": "passwd",
                           "required": "True",
                           "type":"password",
                           }
                    ),
            }

    cpassword=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control my-2",
            "placeholder":"confirm password",
            "id":"cpassword",
            "required":"True",
            }))
    def clean_username(self):
        username = super().clean()["username"]
        min_length = 5
        l=[]
        users=[]
        d = signup.objects.all()
        for i in d:
            users.append(i.username)
        if (username in users) or len(users)==0 :
            raise forms.ValidationError("Username already exists......!")  
        else:
            if len(username) < min_length:
                l.append("Username must have greater than 5 characters")
            if "_" not in list(username):
                l.append("Username must contain _ special character")
            if len(l) != 0:
                raise forms.ValidationError(l)
        return username

    def clean_email(self):
        email = super().clean()["email"]
        l = []
        print(l)
        print(email)
        d = signup.objects.all()
        for i in d:
            l.append(i.email)
        if email in l or len(email)==0:
            raise forms.ValidationError("This email has already been registered")
        return email

    def clean_password(self):
        password=super().clean()["password"]
        #username=self.cleaned_data['username'
        l=[]
        if len(password)<8:
            l.append("password should have atleast 8 characters")
        a=re.search("[A-Z]",password)
        if not a:
            l.append("password should have atleast one uppercase letter")
        b=re.search("[a-z]",password)
        if not b:
            l.append("password should have atleast one lowercase letter")
        c=re.search("[0-9]",password)
        if not c:
            l.append("password should have atleast one digit")
        d=re.search("[!@#$%^&*]",password)
        if not d:
            l.append("password should have atleast one special characters (e.g., !,@,#,$,%,^,*")
        if len(l)!=0:
            raise forms.ValidationError(l)
        return password

    def clean_cpassword(self):
        cleaned_data=super().clean()
        print(cleaned_data)
        a2=cleaned_data.get("password")
        a1=cleaned_data["cpassword"]
        if a1!=a2:
            raise forms.ValidationError("password not matched!.. please verify")
        return a1


class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields=["username"]
        widgets={
        "username":forms.TextInput(
            attrs={
            "class":"form-control my-2",
            "placeholder":"username",
            "id":"username",
            "required":"True",
            }
            )
        }
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control my-2",
            "placeholder":"password",
            "id":"password",
            "required":"True",
            }))
    captcha=CaptchaField()
    def clean_password(self):
        cleaned_data=super().clean()
        print(cleaned_data)
        username=cleaned_data['username']
        password=cleaned_data.get("password")
        
        flag=0
        d=signup.objects.all()
        for i in d:
            if (i.username==username and i.password==password):
                flag=1
                break
        if flag!=1:
            raise forms.ValidationError("invalid user and incorrect password")
        return [username,password]


    def clean_captch(self):
        cleande_data=super().clean()
        a=cleaned_data['captcha']
        if not verify_captcha(a):
            raise forms.ValidationError("Invalid captcha,please verify")
        return a


class review(forms.ModelForm):
    class Meta:
        model=feedbackt
        fields=["comment","query","rating"]
        widgets={
        "comment":forms.TextInput(
            attrs={
            "class":"form-control my-2 'rows'=5 'cols'=5",
            "id":"comment",
            "placeholder":"Comment here ...."
            }),
        "query":forms.Textarea(
            attrs={
            "class": "form-control my-2",  # Add your custom CSS classes if needed
                "placeholder": "Enter any non-translated information ...",
                "cols": 50,  # Adjust the number of columns (width)
                "rows": 5,
                "id":"query"
            })
        }
class Audioform(forms.ModelForm):
    class Meta:
        model=audio
        fields=['audioname']

class quotesform(forms.ModelForm):
  class Meta:
    model = quotesg  # Assuming quotesg is your model name
    fields = ['image', 'name', 'text']
    widgets = {
      "image": forms.ClearableFileInput(
          attrs={
              "class": "form-control my-2",
              "type": "file",
              "placeholder": "Enter author image :",
          }
      ),
      "name": forms.TextInput(
          attrs={
              "class": "form-control my-2",
              "placeholder": "Author name :",
          }
      ),
      "text": forms.Textarea(  # Use Textarea instead of TextInput
          attrs={
              "class": "form-control my-2",
              "placeholder": "Enter quote:",
              "rows": 5,  
              "cols": 50,  
          }
      ),
    }

    def __init(self,*args,**kwargs):
        super(quotesform,self).__init__(*args,**kwargs)
        self.fields['image'].required=True


class superusersignupform(forms.ModelForm):
    class Meta:
        model = superuser
        fields = ["username", "email", "dob", "password"]
        widgets = {
                  "username": forms.TextInput(
                    attrs={
                            "class": "form-control my-2",
                            "placeholder": "user name",
                            "id": "username",
                            }
                    ),
                  "email": forms.EmailInput(
                    attrs={
                            "class": "form-control my-2",
                            "placeholder": "eg@gmail.com",
                            "id": "email",
                            "required": "True",
                            }
                    ),
                  "dob": forms.DateInput(
                    attrs={
                           "class": "form-control my-2",
                           "placeholder": "dd/mm/yyyy",
                           "id": "dob",
                           "type": "date",
                           }
                    ),
                  "password": forms.PasswordInput(
                    attrs={
                           "class": "form-control my-2",
                           "placeholder": "password",
                           "id": "passwd",
                           "required": "True",
                           "type":"password",
                           }
                    ),
            }

    cpassword=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control my-2",
            "placeholder":"confirm password",
            "id":"cpassword",
            "required":"True",
            }))
    def clean_username(self):
        username = super().clean()["username"]
        min_length = 5
        l=[]
        users=[]
        d = superuser.objects.all()
        for i in d:
            users.append(i.username)
        print(users)
        if (username in users):
            raise forms.ValidationError("Username already exists......!")  
        else:
            if len(username) < min_length:
                l.append("Username must have greater than 5 characters")
        if len(l) != 0:
                raise forms.ValidationError(l)
        return username

    def clean_email(self):
        email = super().clean()["email"]
        l = []
        print(l)
        print(email)
        d = superuser.objects.all()
        for i in d:
            l.append(i.email)
        if email in l or len(email)==0:
            raise forms.ValidationError("This email has already been registered")
        return email

    def clean_password(self):
        password=super().clean()["password"]
        #username=self.cleaned_data['username'
        l=[]
        if len(password)<8:
            l.append("password should have atleast 8 characters")
        d=re.search("[!@#$%^&*.]",password)
        if not d:
            l.append("password should have atleast one special characters (e.g., !,@,#,$,%,^,*,.")
        if len(l)!=0:
            raise forms.ValidationError(l)
        return password

    def clean_cpassword(self):
        cleaned_data=super().clean()
        print(cleaned_data)
        a2=cleaned_data.get("password")
        a1=cleaned_data["cpassword"]
        if a1!=a2:
            raise forms.ValidationError("password not matched!.. please verify")
        return a1
class superuserloginform(forms.ModelForm):
    class Meta:
        model=superuserlogin
        fields=["username"]
        widgets={
        "username":forms.TextInput(
            attrs={
            "class":"form-control my-2",
            "placeholder":"username",
            "id":"username",
            "required":"True",
            }
            )
        }
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control my-2",
            "placeholder":"password",
            "id":"password",
            "required":"True",
            }))
    captcha=CaptchaField()
    def clean_password(self):
        cleaned_data=super().clean()
        print(cleaned_data)
        username=cleaned_data['username']
        password=cleaned_data.get("password")
        
        flag=0
        d=superuser.objects.all()
        for i in d:
            if (i.username==username and i.password==password):
                flag=1
                break
        if flag!=1:
            raise forms.ValidationError("invalid user and incorrect password")
        return [username,password]


    def clean_captch(self):
        cleande_data=super().clean()
        a=cleaned_data['captcha']
        if not verify_captcha(a):
            raise forms.ValidationError("Invalid captcha,please verify")
        return a