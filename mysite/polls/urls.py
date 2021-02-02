from django.urls import path


# This is the mysite/polls/urls.py

# only gets consulted by django if the URL starts with
# http://127.0.0.1:8080/polls/

# it defines what django should do for anything after that

from . import views

app_name = 'polls'
# urlpatterns = [
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('',views.index, name ='index'), # http://126.0.0.1:8080/polls/' + ''
#         # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]