from django.contrib.auth import forms, get_user_model, models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Term, Course, ClassNote

class TermForm(forms.ModelForm):
    fields = ('school', 'year', 'session')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = ''

        placeholders = (
            'School name', 'Academic year (numerical value)', 'Academic term'
            )

        for field, placeholder in zip(self.fields, placeholders):
            self.fields[field].widget.attrs.update({'placeholder': placeholder})

    class Meta():
        model = Term
        fields = ('school', 'year', 'session')

class CourseForm(forms.ModelForm):
    fields = ('title', 'course_code', 'term')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('active_user', None)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['term'].queryset = Term.objects.filter(user=user)

        for field in self.fields:
            self.fields[field].label = ''

        placeholders = ('Course title', 'Course code')

        for field, placeholder in zip(self.fields, placeholders):
            self.fields[field].widget.attrs.update({'placeholder': placeholder})

        self.fields['term'].empty_label = 'Academic term'

    class Meta():
        model = Course
        fields = ('title', 'course_code', 'term')

class CoursesOfTermForm(forms.ModelForm):
    fields = ('title', 'course_code')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = ''

        placeholders = ('Course title', 'Course code')

        for field, placeholder in zip(self.fields, placeholders):
            self.fields[field].widget.attrs.update({'placeholder': placeholder})

    class Meta():
        model = Course
        fields = ('title', 'course_code')

class ClassNoteForm(forms.ModelForm):
    fields = ('title', 'body', 'course')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('active_user', None)
        current_course = kwargs.pop('course', None)
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = ''

        self.fields['course'].widget.attrs.update({"class": "w-10"})
        self.fields['title'].widget.attrs.update(
            {"placeholder": "Please enter a title"}
            )
        self.fields['course'].empty_label = 'Select a course'

        if user is not None:
            self.fields['course'].queryset = Course.objects.filter(user=user)

            if current_course is not None:
                self.fields['course'].queryset = current_course

    class Meta():
        model = ClassNote
        fields = ('title', 'body', 'course')

class UpdateNoteForm(forms.ModelForm):
    fields = ('title', 'body', 'course')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = ''

        self.fields['course'].widget.attrs.update({"class": "w-10"})
        self.fields['title'].widget.attrs.update(
            {"placeholder": "Please enter a title"}
            )
        self.fields['course'].empty_label = 'Select a course'

    class Meta():
        model = ClassNote
        fields = ('title', 'body', 'course')

class CurrentTermForm(forms.Form):
    current_term = forms.ChoiceField()

    def __init__(self, term_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['current_term'].label = ''
        self.fields['current_term'].choices = term_choices

class SearchBarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        searchbar_styles = {
            "class": "form-control form-control-dark w-100",
            "placeholder": "Enter note title",
            "aria-label": "Search",
            }
        self.fields['title'].widget.attrs.update(searchbar_styles)
        self.fields['title'].label = ''

    class Meta():
        model = ClassNote
        fields = ('title',)
