from django.urls import path

from . import views


# Adding a namespace to our URLConfs file
app_name = 'polls'

# This was the old way, as in - without using generic views
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name="index"),
#     # ex: /polls/5/
#     # note, the question_id gets passed to the views function
#     path('<int:question_id>/', views.detail, name="detail"),
#     # ex: /poll/5/results/
#     path('<int:question_id>/results/', views.results, name="results"),
#     # ex: /poll/5/vote/
#     path('<int:question_id>/vote/', views.vote, name="vote"),
#     # I just added the below as a test
#     path('test/', views.test, name="test"),
# ]

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    # note, the question_id gets passed to the views function
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    # ex: /poll/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    # ex: /poll/5/vote/
    path('<int:question_id>/vote/', views.vote, name="vote"),
    # I just added the below as a test
    path('test/', views.test, name="test"),
]
