from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [path('', views.event_list, name = 'event_list'),
               path('events/<int:event_id>/', views.event_detail, name = 'event_detail'),
               path('events/create/', views.event_create, name = 'event_create'),
               path('events/<int:event_id>/register/', views.register_event, name = 'register_event'),
               path('my-registrations/', views.my_registration, name = 'my_registrations'),
               path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
               path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
               path('events/<int:event_id>/delete', views.delete_event, name = 'delete_event'),
               path('events/<int:event_id>/edit', views.edit_event, name = 'edit_event'),
               path('register/', views.register_page, name = 'register'),
               path('events/<int:event_id>/leave/', views.leave_event, name = 'leave_event'),
               
               
               ]
