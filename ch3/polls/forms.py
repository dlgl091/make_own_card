from django import forms

class SubmitForm(forms.Form): # ModelForm 은 장고 모델 폼
    cardNo = forms.IntegerField(primary_key=True)
    category = forms.CharField(max_length=10)  # category
    genImgLink = forms.ImageField(null=True, upload_to="", blank=True)  # genImgLink
    text1 = forms.CharField(max_length=20, default="")
    text2 = forms.CharField(max_length=20, default="")