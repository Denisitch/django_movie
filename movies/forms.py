from django import forms

from movies.models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
