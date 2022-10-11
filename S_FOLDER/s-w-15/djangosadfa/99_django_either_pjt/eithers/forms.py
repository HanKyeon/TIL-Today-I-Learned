from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    
    PICK_A=False
    PICK_B=True
    PICKS = [
        (PICK_A, '좌'),
        (PICK_B, '우'),
    ]
    pick = forms.ChoiceField(
        choices=PICKS
    )

    class Meta:
        model = Question
        fields = '__all__'
