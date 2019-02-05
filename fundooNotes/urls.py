"""
urls.py

    Every request that comes to django ,Django send each request to this page first
    this page contains urls for all the pages ,these urls determines where each request can
    be handled and desired response

Author: Saurabh Singh
Since : 4 Feb ,2019
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from users import views as core_views
# from django.conf.urls import urls
from django.conf.urls import url, include
from Notes import views
from Labels import views as label_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('users.urls')),
    path('login/', core_views.user_login, name='login'),
    # path('fundoo-home/',views.home,name='home')
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/',TokenRefreshView.as_view()),
    path('home/', core_views.home, name='home'),
    url(r'^auth/', include('social_django.urls', namespace='social')),

    url('create/', views.create_note, name='create_note'),

    path('shownotes/', views.show_notes, name='show_notes'),

    path('edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('update/<int:pk>/', views.note_update.as_view(), name='note_update'),

    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('delete_note/<int:pk>/', views.note_delete_note.as_view(), name='note_delete_note'),

    path('reminder/<int:pk>/', views.note_reminder, name='note_reminder'),
    # path('reminder_save/<int:pk>/', views.reminder_save, name='reminder_save'),

    # path('note_reminder/',views.note_reminder),

    path('index/', views.index, name='pagination'),
    path('lazy_load_notes/', views.lazy_load_notes, name='lazy_load_notes'),

    path('copy/<int:pk>/', views.copy_note, name='copy_note'),
    path('archive/<int:pk>/', views.archive, name='archive'),
    path('show_archive/', views.show_archive_notes, name='show_archive_notes'),

    path('pin/<int:pk>/', views.pin, name='pin'),
    path('show_pin_notes', views.show_pin_notes, name='show_pin_notes'),

    path('show_trash_notes', views.show_trash_notes, name='show_trash_notes'),

# --------------- Labels-------------------------------------------------------
    path('create_label/',label_views.create_label,name='create_label'),
    path('update_label/<int:pk>/',label_views.update_label,name='update_label')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
