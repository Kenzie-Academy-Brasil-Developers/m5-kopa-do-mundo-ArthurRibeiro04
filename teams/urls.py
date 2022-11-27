from django.urls import path
from .views import TeamView, TeamWithParamsViews

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:team_id>/', TeamWithParamsViews.as_view())
]
