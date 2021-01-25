from django.urls import path
from polls import views

urlpatterns = [
    path('', views.pollsindex),
    path('pollsindex/', views.pollsindex2),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('display/', views.display),
    path('dis/', views.dis),
]