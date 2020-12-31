from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Endless.models import ListUser, Post

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ListUser
        fields = ('username', 'profile_pic')

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # 这里一定要用pop,而不是get,
        # 因为form的__init__方法并没有"request"这个参数
        self.request = kwargs.pop("request", None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.author = self.request.user
        return super(PostForm, self).save(commit=True)

    class Meta:
        model = Post
        fields = ['title','description','link','image','media_type']