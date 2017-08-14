import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import PostForm, TodoForm, GoalForm, BookForm, CourseForm, EventForm, FeatureForm, StudyForm, RoughTDFORM, SideProjForm, DedicatedSLForm, IdeaForm, BookDelForm, FeatureDelForm, SPDelForm, CourseDelForm, SLDelForm, TDDelForm, EventDelForm, IdeaDelForm, \
    RoughTodoDelForm, PersonDelForm
from .models import Blog_post, Todo_list, Goal_list, Book_list, Course_list, Event_list, Feature_list, Quote_list, Puzzle_list, Study_Plan, Rough_TODO, Side_Projects, Dedicated_SL, Idea_Brainstorm, \
    Person_list

#TODO: NEED TO GO THROUGH THE ENTIRE VIEWS CODE AND RE-CODE IT PROPERLY

##################
# Main Page
##################

class IndexView(ListView):
    context_object_name = 'home_list'
    template_name = 'main.html'
    queryset = Todo_list.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['goals'] = Goal_list.objects.all()
        context['events'] = Event_list.objects.all().order_by('-pk')
        context['quotes'] = random.choice(Quote_list.objects.all())
        context['person'] = Person_list.objects.all()
        context['side_projects'] = Side_Projects.objects.all().order_by('-pk')[:1]
        context['book'] = Book_list.objects.all()[:3]
        context['people']=Person_list.objects.all()[:3]
        context['courses']=Course_list.objects.all()[:3]
        # context['book_ec'] = collect.get_random_book()
        # context['linkedin_rec'] = linkedin_recommend.get_random_rec()

        return context


##################
# Side Project Section
##################

class SecondView(ListView):
    context_object_name = 'side_project'
    template_name = 'side_project.html'
    queryset = Side_Projects.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SecondView, self).get_context_data(**kwargs)
        context['ideas'] = Idea_Brainstorm.objects.all().order_by('content')
        context['category'] = ['Script_C', 'Script_F', 'SP_current', 'SP_future', 'Script_I', 'SP_I']
        return context


##################
# Blog Section
##################

def post_detail(request, slug=None, id=None):
    instance = get_object_or_404(Blog_post, id=id)
    context = {
        "title": instance.name,
        "body": instance.content,
        "date": instance.pub_date,
        "id": instance.id,
    }
    return render(request, "post_detail.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Blog_post, id=id)
    instance.delete()
    return redirect("blog_list")

def post_update(request, slug=None, id=None):
    instance = get_object_or_404(Blog_post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # return HttpResponseRedirect(instance.get_absolute_url())
        return HttpResponseRedirect(reverse('blog_list'))

    context = {
        "title": instance.name,
        "instance": instance.content,
        "form": form,
    }
    return render(request, "post_update.html", context)

def pag(a, request):
    paginator = Paginator(a, 5)
    page = request.GET.get('page')
    try:
        blog_post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_post = paginator.page(paginator.num_pages)
    return blog_post

def blog(request):
    all_entires = Blog_post.objects.all().order_by('-pk')
    research_entires = Blog_post.objects.filter(category='Research').order_by('-pk')
    interest_entires = Blog_post.objects.all().filter(category='Interest').order_by('-pk')
    script_entires = Blog_post.objects.filter(category='Script').order_by('-pk')
    school_entires = Blog_post.objects.filter(category='School').order_by('-pk')

    # x = pag(all_entires, request)
    f = request.POST.get('category') #request changes everytime;
    li = ['Interest', 'Research', 'Script', 'School']

    # if f != None:
    #     request.session['0'] = f

    # if request.session['0'] == 'Interest':
    #     return render(request, "blog_list.html", {'object_list': pag(interest_entires, request)})
    # if f != None or request.session['0'] in li:
    #     # request.session['0'] = f
    #     if f == 'Interest':
    #         return render(request, "blog_list.html", {'object_list': pag(interest_entires, request)})

    return render(request, "blog_list.html", {'object_list': pag(all_entires, request)})

    # paginator = Paginator(all_entires, 5)
    #
    # page = request.GET.get('page')
    #
    # try:
    #     blog_post = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     blog_post = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     blog_post = paginator.page(paginator.num_pages)

    # x = pag(all_entires, request)
    # f = request.POST.get('category')
    # li = ['Interest', 'Research', 'Script', 'School']
    # print(request.session[0])
    # if f != None or request.session[0] in li:
    #     request.session[0] = f
    #     if f == 'interest':
    #         return render(request, "blog_list.html", {'object_list': pag(interest_entires, request)})
    #
    # request.session[0] = 'mon'
    # return render(request, "blog_list.html", {'object_list': x})
    # request.session[0] = 'Interest'
    # if f == 'Interest' or request.session[0] == 'Interest':
    #     return render(request, "blog_list.html", {'object_list': pag(interest_entires, request)})

    # TODO: right now, request.session is being overwritten with mon everyday you click...
    #
    # request.session[0] = 'mon'
    # print(request.session.get(0))
    # if f == 'Interest' or 'Interest' in request.session[0]:
    #     del request.session[0]
    #     request.session[0] = 'Interest'
    #     print(request.session.get(0))
    #     return render(request, "blog_list.html", {'object_list': pag(interest_entires, request)})
    # if request.POST.get('category') == 'Research' or request.session[0] == 'Research':
    #     request.session[0] = 'Research'
    #     return render(request, "blog_list.html", {'object_list': research_entires})
    #
    # if request.POST.get('category') == 'Script':
    #     return render(request, "blog_list.html", {'object_list': script_entires})
    #
    # if request.POST.get('category') == 'School':
    #     return render(request, "blog_list.html", {'object_list': school_entires})

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    f = PostForm(initial={'content': '<li></li>'})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # return HttpResponseRedirect(instance.get_absolute_url())
        return HttpResponseRedirect(reverse('blog_list'))

    context = {
        "form": form,
        'prefill': f,
    }
    return render(request, "post_form.html", context)

##################
# To-Do Section
##################
def todo_create(request):
    form = TodoForm(request.POST or None)
    pre = TodoForm(initial={'content': '<br/>'})

    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('home_list'))

    context = {
        "form": form,
        "pre": pre,
    }
    return render(request, "todo_create.html", context)

# def person_create(request):
#     form = PersonForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(reverse('home_list'))
#
#     context = {
#         "form": form,
#     }
#     return render(request, "person_create.html", context)


def goal_create(request):
    form = GoalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('home_list'))

    context = {
        "form": form,
    }
    return render(request, "goal_create2.html", context)

def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('home_list'))

    context = {
        "form": form,
    }
    return render(request, "event_create.html", context)




def book_list(request):
    book_query = Book_list.objects.all().order_by('-pk')

    context = {
        "object_list": book_query,
    }
    return render(request, "book_list.html", context)

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('book_list'))

    context = {
        "form": form,
    }
    return render(request, "book_create.html", context)

def course_list(request):
    course_query = Course_list.objects.all().order_by('pk')
    context = {
        "object_list": course_query,
        "title": "List of Courses",
    }
    return render(request, "course_list.html", context)

def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('course_list'))

    context = {
        "form": form,
    }
    return render(request, "course_create.html", context)


def feature_list(request):
    priority_query = Feature_list.objects.all().filter(content__startswith='Priority')
    feature_query = Feature_list.objects.all().filter(content__startswith='Not-Priority')
    temp_query = Feature_list.objects.all()
    context = {
        "priority_list": priority_query,
        "notpriority_list": feature_query,
        "temp_list": temp_query,
    }
    return render(request, "feature_list.html", context)

def feature_create(request):
    form = FeatureForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('feature_list'))

    context = {
        "form": form,
    }
    return render(request, "feature_create.html", context)

def study_plan(request):
    study_query = Study_Plan.objects.all().order_by('-pk')
    context = {
        "object_list": study_query,
    }
    return render(request, "study_plan.html", context)

def study_create(request):
    form = StudyForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('study_plan'))

    context = {
        "form": form,
    }
    return render(request, "study_create.html", context)

def roughTD_list(request):
    roughTD_query = Rough_TODO.objects.all()
    context = {
        "object_list": roughTD_query,
    }
    return render(request, "rough_todo.html", context)

def roughTD_create(request):
    form = RoughTDFORM(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('rough_todo'))

    context = {
        "form": form,
    }
    return render(request, "roughtd_create.html", context)

def roughTD_delete(request, new_id):
    instance = get_object_or_404(Rough_TODO, id=new_id)
    if request.method == 'POST':
        form = RoughTodoDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('rough_todo')

    else:
        form = RoughTDFORM(instance=instance)

    context = {
        'form': form,
    }

    return render(request, 'rough_todo.html', context)


# def side_projects(request):
#     script_current = Side_Projects.objects.all().filter(category='Script_Current')
#     sideproject_query = Side_Projects.objects.all()
#     sp_rand = Side_Projects.objects.all().filter(category=Side_Projects.SCRIPT_CURRENT)
#     class_ra = Side_Projects.is_upperclass(0)
#
#     context = {
#         "category_choices": 'adslkahsldkj',
#     }
#
#     return render(request, "side_project.html", context)

def sideproject_add(request):
    form = SideProjForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('home_list'))

    context = {
        "form": form,
    }
    return render(request, "sideproject_create.html", context)

def dedicated_sl(request):
    dedicatedsl_query = Dedicated_SL.objects.all()
    context = {
        "object_list": dedicatedsl_query,
    }
    return render(request, "dedicated_self.html", context)

def dedicatedsl_add(request):
    form = DedicatedSLForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('dedicated_sl'))

    context = {
        "form": form,
    }
    return render(request, "dedicatedself_create.html", context)

def idea_add(request):
    form = IdeaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(reverse('side_project'))

    context = {
        "form": form,
    }
    return render(request, "idea_create.html", context)

def book_selected(request, new_id):
    instance = get_object_or_404(Book_list, id=new_id)
    if request.method == 'POST':
        form = BookDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return HttpResponseRedirect(reverse_lazy('book_list'))

    else:
        form = BookDelForm(instance=instance)

    context = {
        'form': form
    }
    return render(request, 'book_list.html', context)

def feature_selected(request, new_id):
    instance = get_object_or_404(Feature_list, id=new_id)
    if request.method == 'POST':
        form = FeatureDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('feature_list')

    else:
        form = FeatureDelForm(instance=instance)

    context = {
        'form': form
    }
    return render(request, 'feature_list.html', context)

def sp_selected(request, new_id):
    if request.method == 'POST' and 'sp_delete' in request.POST:
        instance = get_object_or_404(Side_Projects, id=new_id)
        form = SPDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('home_list')

        else:
            form = SPDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'side_project.html', context)

    elif request.method =='POST' and 'idea_delete' in request.POST:
        instance = get_object_or_404(Idea_Brainstorm, id=new_id)
        form = IdeaDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('side_project')

        else:
            form = IdeaDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'side_project.html', context)

def course_selected(request, new_id):

    if request.method == 'POST':
        instance = get_object_or_404(Course_list, id=new_id)
        form = CourseDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('course_list')

        else:
            form = CourseDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'course_list.html', context)

def course_edit(request, new_id):
    instance = get_object_or_404(Course_list, id=new_id)
    form = CourseForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('course_list')

    context = {
        'form': form,
        'title': instance.title,
        'school': instance.school,
        'timeframe': instance.timeframe,
        'commitment': instance.commitment,
        'url': instance.url,
    }
    return render(request, 'course_edit.html', context)

def sl_selected(request, new_id):

    if request.method == 'POST' and 'delete_sl' in request.POST:
        instance = get_object_or_404(Dedicated_SL, id=new_id)
        form = SLDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('dedicated_sl')

        else:
            form = SLDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'dedicated_self.html', context)

def sl_edit(request, new_id):
    instance = get_object_or_404(Dedicated_SL, id=new_id)
    form = DedicatedSLForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(reverse('dedicated_sl'))

    context = {
        'form': form,
        'title': instance.title,
        'content': instance.content,
    }
    return render(request, "selflearning_edit.html", context)

def roughTD_edit(request, new_id):
    instance = get_object_or_404(Rough_TODO, id=new_id)
    form = RoughTDFORM(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('rough_todo')

    context = {
        'form': form,
        'title': instance.title,
        'content': instance.content,
    }
    return render(request, 'roughTD_edit.html', context)

def todo_edit(request, new_id):
    instance = get_object_or_404(Todo_list, id=new_id)
    form = TodoForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('home_list')

    context = {
        'form': form,
        'content': instance.content
    }
    return render(request, 'todo_edit.html', context)

def event_edit(request, new_id):
    instance = get_object_or_404(Event_list, id=new_id)
    form = EventForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('home_list')

    context = {
        'form': form,
        'name': instance.name,
        'start_time': instance.start_time,
        'end_time': instance.end_time,
        'event_url': instance.event_url,
        'date': instance.date,
    }
    return render(request, 'event_edit.html', context)

def feature_edit(request, new_id):
    instance = get_object_or_404(Feature_list, id=new_id)
    form = FeatureForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('feature_list')

    context = {
        'form': form,
        'content': instance.content,
    }
    return render(request, 'feature_edit.html', context)

def sideproject_edit(request, new_id):
    instance = get_object_or_404(Side_Projects, id=new_id)
    form = SideProjForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('home_list')

    context = {
        'form': form,
        'title': instance.title,
        'content': instance.content,
        'days': instance.days,
        # 'timeframe': instance.timeframe,
        # 'resources': instance.resources,
    }
    return render(request, 'sideproject_edit.html', context)


def ideabrain_edit(request, new_id):
    instance = get_object_or_404(Idea_Brainstorm, id=new_id)
    form = IdeaForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('side_project')

    context = {
        'form': form,
        'content': instance.content,
    }
    return render(request, 'ideabrain_edit.html', context)

def tdevent_selected(request, new_id):

    # Todo form
    if request.method == 'POST' and 'todo_delete' in request.POST:
        instance = get_object_or_404(Todo_list, id=new_id)
        if request.method == 'POST':
            form = TDDelForm(request.POST, instance=instance)

            if form.is_valid():
                instance.delete()
                return redirect('home_list')

        else:
            form = TDDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'main.html', context)

    # Event form
    elif request.method == 'POST' and 'event_delete' in request.POST:
        instance = get_object_or_404(Event_list, id=new_id)
        form = EventDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('home_list')

        else:
            form = EventDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'main.html', context)

    # Person form
    elif request.method == 'POST' and 'person_delete' in request.POST:
        instance = get_object_or_404(Person_list, id=new_id)
        form = PersonDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect(reverse('home_list'))

        else:
            form = PersonDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'main.html', context)

def studyplan_selected(request, new_id):
    instance = get_object_or_404(Study_Plan, id=new_id)
    if request.method == "POST":
        form = SPDelForm(request.POST, instance=instance)

        if form.is_valid():
            instance.delete()
            return redirect('study_plan')

        else:
            form = SPDelForm(instance=instance)

        context = {
            'form': form
        }
        return render(request, 'study_plan.html', context)


def studyplan_edit(request, new_id):
    instance = get_object_or_404(Study_Plan, id=new_id)
    form = StudyForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('study_plan')

    context = {
        'form': form,
        'title': instance.title,
        'content': instance.content,
    }
    return render(request, 'studyplan_edit.html', context)

def test_new(request):
    return render(request, 'main2.html')

def test_view(request):
    instance = random.choice(Puzzle_list.objects.all())
    context = {
        'queryset': instance
    }
    return render(request, 'test_view.html', context)






# def feature_edit(request, new_id):
#     instance = get_object_or_404(Feature_list, id=new_id)
#     form = FeatureForm(request.POST or None, instance=instance)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return redirect('feature_list')
#
#     context = {
#         'form': form,
#         'content': instance.content,
#     }
#     return render(request, 'feature_edit.html', context)




# def todo_selected(request, new_id):
#     instance = get_object_or_404(Todo_list, id=new_id)
#     if request.method == 'POST':
#         form = TDDelForm(request.POST, instance=instance)
#
#         if form.is_valid():
#             instance.delete()
#             return redirect('home_list')
#
#     else:
#         form = TDDelForm(instance=instance)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'time.html', context)
#
# def event_selected(request, new_id):
#     instance = get_object_or_404(Event_list, id=new_id)
#     if request.method == 'POST':
#         form = EventDelForm(request.POST, instance=instance)
#
#         if form.is_valid():
#             instance.delete()
#             return redirect('home_list')
#
#     else:
#         form = EventDelForm(instance=instance)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'time.html', context)

# def sl_edit(request, new_id):
#     instance = get_object_or_404(Dedicated_SL, id=new_id)
#
#     if request.method == 'POST' and 'edit' in request.POST:
#         form = DedicatedSLForm(request.POST or None, instance=instance)
#
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             return redirect(reverse('dedicated_sl'))
#
#     context = {
#         "title": instance.title,
#         "content": instance.content,
#     }
#     return render(request, "selflearning_edit.html", context)



# if request.method == 'POST' and 'edit_sl' in request.POST:
    #     instance = get_object_or_404(Dedicated_SL, id=new_id)
    #     form = DedicatedSLForm(request.POST, instance=instance)
    #
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.save()
    #         return redirect('dedicated_sl')
    #
    #     context = {
    #         'title': instance.title,
    #         'content': instance.content,
    #         'form': form,
    #     }
    #     return render(request, 'selflearning_edit.html', context)

        # def blog(request):
        #     all_entires = Blog_post.objects.all()
        #     context = {
        #         "object_list": all_entires,
        #         "title": "List of Entries"
        #     }
        #     return render(request, "blog_list.html", context)

        # def puzzle_input(request):
        #     form = PuzzleCheckForm(request.POST or None)
        #     if form.is_valid():
        #         instance = form.save(request.POST or None)
        #         instance.save()
        #         return redirect('home_list')
        #
        #     context ={
        #         "form": form,
        #     }
        #     return render(request, 'puzzle_input.html', context)


        # def todo_create(request):
        #     form = TodoForm(request.POST or None)
        #     if form.is_valid():
        #         instance = form.save(commit=False)
        #         print(form.cleaned_data.get("title"))
        #         instance.save()
        #         return HttpResponseRedirect(reverse('home_list'))
        #
        #     context = {
        #         "form": form,
        #     }
        #     return render(request, "todo_create.html", context)

        # def feature_selected(request, new_id):
        #     instance = get_object_or_404(Feature_list, id=new_id)
        #     if request.method == 'POST':
        #         form = FeatureDelForm(request.POST, instance=instance)
        #
        #         if form.is_valid():
        #             instance.delete()
        #             return redirect('feature_list')
        #
        #     else:
        #         form = FeatureDelForm(instance=instance)
        #
        #     context = {
        #         'form': form
        #     }
        #     return render(request, 'feature_list.html', context)



# def puzzles(request):
#     puzzle_queryset = Puzzle_list.objects.all()
#     context = {
#         "object_list": puzzle_queryset,
#     }
#     return render(request, 'puzzle.html', context)
#
# def puzzle_answer(request):
#     form = PuzzleCheckForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(request.POST or None)
#         instance.save()
#         return redirect('puzzle_list')
#
#     # its something with this line below:
#     # if form == Puzzle_list.objects.all()
#     context = {
#         'form': form,
#     }
#     return render(request, 'puzzle.html', context)
