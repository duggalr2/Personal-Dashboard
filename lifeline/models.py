from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.core.files.storage import FileSystemStorage

class Blog_post(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateField(default=date.today)

    research = 'Research'
    interest = 'Interest'
    script = 'Script'
    school = 'School'

    Category_Choices = (
        (research, 'Research'),
        (interest, 'Interest'),
        (script, 'Script'),
        (school, 'School')
    )
    # category_choice = models.CharField(max_length=150, choices=Category_Choices, default=interest)
    category = models.CharField(max_length=150, choices=Category_Choices, default=interest)
    fs = FileSystemStorage(location='/media')
    screen_shot = models.ImageField(storage=fs, blank=True)
    # category = models.CharField(max_length=150, choices=Category_Choices, default=interest)

class Todo_list(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

class Goal_list(models.Model):
    title = models.CharField(max_length=150, default='SOME STRING')
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Book_list(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_list", kwargs={"id": self.id})

class Course_list(models.Model):
    title = models.CharField(max_length=250)
    school = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=150, default='timeframe')
    commitment = models.TextField(default='ENTER SYLLABUS SUMMARY HERE')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Event_list(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    event_url = models.URLField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class Ran_event_list(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.TimeField(default=datetime.now().time())
    date = models.DateField(default=date.today)

class Person_list(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

class Feature_list(models.Model):
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.content

class Quote_list(models.Model):
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.content

class Puzzle_list(models.Model):
    content = models.TextField()
    answer = models.TextField(default='SOME STRING')
    input_answer = models.TextField(default='SOME STRING')

    def __str__(self):
        return self.content

class Study_Plan(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title

class Rough_TODO(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title

class Side_Projects(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    days = models.IntegerField(default=7)
    # timeframe = models.CharField(max_length=300)
    #
    # SCRIPT_CURRENT = 'Script_C'
    # SCRIPT_FUTURE = 'Script_F'
    # SP_CURRENT = 'SP_current'
    # SP_FUTURE = 'SP_future'
    # SCRIPT_I = 'Script_I'
    # SP_I = 'SP_I'
    #
    # Category_Choices = (
    #     (SCRIPT_CURRENT, 'Script_Current'),
    #     (SCRIPT_FUTURE, 'Script_Future'),
    #     (SP_CURRENT, 'SideProject_Current'),
    #     (SP_FUTURE, 'SideProject_Future'),
    #     (SCRIPT_I, 'Script_Idea'),
    #     (SP_I, 'SideProject_Idea'),
    # )
    #
    # HIGH = '2'
    # LOW = '1'
    #
    # Integer_Choices = (
    #     (HIGH, '2'),
    #     (LOW, '1')
    # )
    #
    # category = models.CharField(max_length=60, choices=Category_Choices, default=SCRIPT_CURRENT)
    # resources = models.CharField(max_length=500, default='Url', blank=True)
    # weight = models.CharField(max_length=60, choices=Integer_Choices, default=LOW)

class Idea_Brainstorm(models.Model):
    content = models.CharField(max_length=350)

    def __str__(self):
        return self.content

class Dedicated_SL(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class TestView(models.Model):
    content = models.TextField()

