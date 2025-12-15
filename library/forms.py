from django import forms
from .models import BookIssue

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['book']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_book(self):
        book = self.cleaned_data.get('book')

        # 🔒 Minimum 1 copy must remain in library
        if book.available_copies <= 1:
            raise forms.ValidationError(
                "This book cannot be issued. At least 1 copy must remain in the library."
            )

        return book
