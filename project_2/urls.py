"""project_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from lifeline import views
from multiurl import multiurl

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.IndexView.as_view(), name='home_list'),
    url(r'^blog/', views.blog, name='blog_list'),
    url(r'^test/', views.post_create, name='post_create'),

    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<id>\d+)/update/$', views.post_update, name='post_update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^todo/', views.todo_create, name='todo_create'),
    # url(r'^perscrea/', views.person_create, name='person_create'),
    url(r'^goal/', views.goal_create, name='goal_create'),
    url(r'book/', views.book_list, name='book_list'),
    url(r'book_create/', views.book_create, name='book_create'),
    url(r'course/studyplan/$', views.study_plan, name='study_plan'),
    url(r'sp/create/$', views.study_create, name='study_create'),
    url(r'^(?P<new_id>\d+)/stud/$', views.studyplan_selected, name='studyplan_selected'),
    url(r'^(?P<new_id>\d+)/spedit/$', views.studyplan_edit, name='studyplan_edit'),
    url(r'course/', views.course_list, name='course_list'),
    url(r'course_create/', views.course_create, name='course_create'),
    url(r'^(?P<new_id>\d+)/cd/$', views.course_selected, name='course_selected'),

    url(r'^(?P<new_id>\d+)/coursedit/$', views.course_edit, name='course_edit'),

    url(r'event_create/', views.event_create, name='event_create'),
    url(r'features/', views.feature_list, name='feature_list'),
    url(r'^(?P<new_id>\d+)/feature/$', views.feature_selected, name='feature_selected'),
    url(r'feature_create/', views.feature_create, name='feature_create'),
    url(r'^(?P<new_id>\d+)/fedit/$', views.feature_edit, name='feature_edit'),
    url(r'rough_todo/', views.roughTD_list, name='rough_todo'),
    url(r'roughtd_create/', views.roughTD_create, name='roughTD_create'),
    url(r'^(?P<new_id>\d+)/rtd/$', views.roughTD_delete, name='roughTD_delete'),
    url(r'^(?P<new_id>\d+)/rtded/$', views.roughTD_edit, name='roughTD_edit'),
    url(r'^(?P<new_id>\d+)/tde/$', views.tdevent_selected, name='tdevent_selected'),
    url(r'sideprojects/', views.SecondView.as_view(), name='side_project'),
    url(r'sp_create/', views.sideproject_add, name='sp_create'),
    url(r'^(?P<new_id>\d+)/s/$', views.sp_selected, name='sp_selected'),
    url(r'ded_sl/', views.dedicated_sl, name='dedicated_sl'),
    url(r'sl_create/', views.dedicatedsl_add, name='dedicatedsl_create'),

    url(r'^(?P<new_id>\d+)/sle/$', views.sl_selected, name='sl_selected'),
    url(r'^(?P<new_id>\d+)/sledit/$', views.sl_edit, name='sl_edit'),

    url(r'^(?P<new_id>\d+)/todoedit/$', views.todo_edit, name='todo_edit'),
    url(r'^(?P<new_id>\d+)/evtedit/$', views.event_edit, name='event_edit'),
    url(r'^(?P<new_id>\d+)/sideprojedit/$', views.sideproject_edit, name='sideproject_edit'),
    url(r'^(?P<new_id>\d+)/ideabrainedit/$', views.ideabrain_edit, name='ideabrain_edit'),

    url(r'idea/', views.idea_add, name='idea_add'),
    url(r'^(?P<new_id>\d+)/f/$', views.book_selected, name='book_selected'),
    # url(r'puzzle/', views.puzzles, name='puzzle_list'),
    # url(r'puz_add/', views.puzzle_answer, name='puzzle_answer'),
    url(r'test_view/', views.test_view, name='test_view'),
    url(r'new/', views.test_new, name='test_new'),
]

# url(r'^delete_book/(?P<new_id>[\w]+)/$', views.book_delete, name='book_delete'),
# url(r'^delete-book/(?P<new_id>[\w]+)/$', views.book_delete, name='book_delete'),
