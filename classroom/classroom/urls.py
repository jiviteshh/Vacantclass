from django.urls import path
from finder.views import home, post_room, remove_room, feedback_view  # Fixed import
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('post/', post_room, name='post'),
    path('remove/', remove_room, name='remove'),
    path("submit-feedback/", feedback_view, name="submit_feedback")
]

urlpatterns += staticfiles_urlpatterns()  # Fixed static files