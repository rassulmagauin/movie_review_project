from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    def __int__(self, *args, **kwargs):
        super(ModelForm,self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'from-control'})
        self.fields['watchAgain'].widget.attrs.update({'class':'from-check-input'})
    
    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        labels = {'watchAgain':('Watch Again')}
        widgets = {'text':Textarea(attrs={'rows':4}),}

