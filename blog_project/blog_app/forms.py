from django import forms
from .models import BlogPost, Comment
from django_ckeditor_5.widgets import CKEditor5Widget

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'login-input'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'login-input'}),
    )

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['created_at']
        fields = ('title', 'content')

        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = False
        self.fields["content"].required = False        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '',  # 'text' 필드의 라벨을 빈 문자열로 설정
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-text',
            'rows': '4',
            'cols': '100',
        })
