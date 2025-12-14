from django import forms
from .models import BookIssue
from django.conf import settings


class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['book']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get current user
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        # Max 2 books per user
        if self.user:
            issued_count = BookIssue.objects.filter(
                user=self.user,
                is_returned=False
            ).count()
            if issued_count >= 2:
                raise forms.ValidationError(
                    "You can issue only 2 books at a time."
                )

        # Check book availability
        book = cleaned_data.get('book')
        if book and book.available_copies <= 0:
            raise forms.ValidationError(
                "This book is currently unavailable."
            )

        return cleaned_data