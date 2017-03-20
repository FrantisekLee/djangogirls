 from django import forms
 from djangogirls.blog.models import Post

 class PostForm(forms.ModelForm):
     class Meta:
         model = Post
         fields = ('title', 'text',)
