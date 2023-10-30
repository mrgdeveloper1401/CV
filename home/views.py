from django.shortcuts import render
from .models import NvbarModel, HeaderConetent, HeaderConetentSciol, AboutMeModels, SkillModel, ExpreiencModel, ExprienceProjec
from django.views import View


class HomeView(View):
    def get(self, request):
        pass