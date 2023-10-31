from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about_me/<int:user_id>/', views.AboutMeView.as_view(), name='about_me'),
    path('sciol/<int:user_id>', views.SciolView.as_view(), name='sciol'),
    path('skill/<int:user_id>', views.SkillView.as_view(), name='skill'),
    path('education/<int:user_id>', views.EducationView.as_view(), name='education'),
    path('exprience/<int:user_id>', views.ExprienceWorkView.as_view(), name='exprience'),
    path('project/<int:user_id>', views.ProjectView.as_view(), name='project'),
    
]
