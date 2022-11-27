from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.forms.models import model_to_dict

import ipdb

from .models import Team


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        team_data = request.data
        
        team = Team.objects.create(
            name=team_data["name"],
            titles=team_data["titles"],
            top_scorer=team_data["top_scorer"],
            fifa_code=team_data["fifa_code"],
            founded_at=team_data["founded_at"]
        )
        
        return Response(model_to_dict(team), 201)
    
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        
        teams_dict = []
        
        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
            
        return Response(teams_dict, 200)
        

class TeamWithParamsViews(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"Error: Team not found"}, 404)
            
        team_dict = model_to_dict(team)
        
        return Response(team_dict, 200)
    
    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"Error: Team not found"}, 404)
        
        team.delete()
        
        return Response({}, 204)
    
    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"Error: Team not found"}, 404)
        
        update_team = request.data
        
        for key, value in update_team.items():
            setattr(team, key, value)
        
        team.save()
        
        team_dict = model_to_dict(team)
        
        return Response(team_dict, 200)

            
            

