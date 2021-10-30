from django import forms

from blog.models import PostCommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = PostCommentModel
        exclude = ["post", "created_at"]
