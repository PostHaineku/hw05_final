from django import forms
from .models import Post
from .models import Group
from .models import Comment


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea,
                           label="Текст",
                           help_text="Текст вашего поста")
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=False,
                                   label="Группа, к которой относится пост",
                                   help_text="Выберите группу")

    class Meta:
        model = Post
        fields = ("text", "group", "image")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
