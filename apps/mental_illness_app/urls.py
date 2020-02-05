from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^process/registration$', views.process_registration),
    url(r'^process/login$', views.process_login),
    url(r'^registration/success$', views.registration_success),
    url(r'^homepage$', views.homepage),
    url(r'^homepage/edit$', views.edit_account),
    url(r'^homepage/edit/update$', views.update_account),
    url(r'^homepage/(?P<user_id>\d+)/delete$', views.delete_account),
    url(r'^homepage/delete/confirmation$', views.delete_confirmation),
    url(r'^goals$', views.view_goals),
    url(r'^goals/(?P<goal_id>\d+)/edit$', views.edit_goal),
    url(r'^goals/(?P<goal_id>\d+)/update$', views.update_journal),
    url(r'^journals$', views.journal),
    url(r'^journals/new$', views.new_journal),
    url(r'^journals/(?P<journal_id>\d+)/edit$', views.edit_journal),
    url(r'^journals/(?P<journal_id>\d+)/delete$', views.delete_journal),
    url(r'^drawing$', views.drawing),
    url(r'^homepage/panic$', views.panic_attack),
]