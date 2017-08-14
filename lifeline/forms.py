from django import forms

from .models import Blog_post, Todo_list, Goal_list, Puzzle_list, Book_list, Course_list, Event_list, Feature_list, Study_Plan, Rough_TODO, Side_Projects, Dedicated_SL, Idea_Brainstorm, Person_list

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = [
            "name",
            "content",
            "pub_date",
            "category",
            "screen_shot",
        ]

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_list
        fields = [
            "content",
        ]

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal_list
        fields = {
            "title",
            "content",
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book_list
        fields = {
            "title",
            "author",
            "category",
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person_list
        fields = {
            'name',
            'position'
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course_list
        fields = {
            "title",
            "school",
            "timeframe",
            "commitment",
            "url",
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event_list
        fields = {
            "name",
            "start_time",
            "end_time",
            "date",
            "event_url",
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature_list
        fields = {
            "content",
        }

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study_Plan
        fields = {
            "title",
            "content",
        }

class RoughTDFORM(forms.ModelForm):
    class Meta:
        model = Rough_TODO
        fields = {
            "title",
            "content",
        }

class SideProjForm(forms.ModelForm):
    class Meta:
        model = Side_Projects
        fields = {
            "title",
            "content",
            "days",
        }

class DedicatedSLForm(forms.ModelForm):
    class Meta:
        model = Dedicated_SL
        fields = {
            "title",
            "content",
        }

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea_Brainstorm
        fields = {
            "content",
        }

class BookDelForm(forms.ModelForm):
    class Meta:
        model = Book_list
        fields = []

class FeatureDelForm(forms.ModelForm):
    class Meta:
        model = Feature_list
        fields = []

class SPDelForm(forms.ModelForm):
    class Meta:
        model = Side_Projects
        fields = []

class IdeaDelForm(forms.ModelForm):
    class Meta:
        model = Idea_Brainstorm
        fields = []

class CourseDelForm(forms.ModelForm):
    class Meta:
        model = Course_list
        fields = []

class SLDelForm(forms.ModelForm):
    class Meta:
        model = Dedicated_SL
        fields = []

class TDDelForm(forms.ModelForm):
    class Meta:
        model = Todo_list
        fields = []

class EventDelForm(forms.ModelForm):
    class Meta:
        model = Event_list
        fields = []

class StudyPlDelForm(forms.ModelForm):
    class Meta:
        model = Study_Plan
        fields = []

class RoughTodoDelForm(forms.ModelForm):
    class Meta:
        model = Rough_TODO
        fields = []

class PuzzleCheckForm(forms.ModelForm):
    class Meta:
        model = Puzzle_list
        fields = [
            "input_answer"
        ]

class PersonDelForm(forms.ModelForm):
    class Meta:
        model = Person_list
        fields = []

class BookTitle(forms.ModelForm):
    class Meta:
        model = Book_list
        fields = [
            'title'
        ]

