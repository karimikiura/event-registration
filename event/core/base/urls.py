from django.urls import path 


from .views import (home_page, event_page, registration_confirmation,
                        profile_page, account_page, project_submission,
                        update_submission,)

# namespace
app_name = 'event'

urlpatterns = [
    path('', home_page, name='index'),
    path('user/<str:pk>/', profile_page, name='profile'),
    path('account/', account_page, name='account'),
    path('event/<str:event_id>/', event_page, name='event'),
    path('registration-confirmation/<str:event_id>/', registration_confirmation, name='confirmation'),
    path('project-submission/<str:pk>/', project_submission, name='submission'),
    path('update-submission/<str:pk>/', update_submission, name='update-submission'),

]