from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_done

from .views import download_resume
from .views import edit_profile_view
from .views import profile_detail_view
from .views import signup

app_name = 'account'
urlpatterns = [
    url(r'^$', profile_detail_view, name='detail'),
    url(r'^edit/$', edit_profile_view, name='edit'),
    url(r'^download-resume/$', download_resume, name='download-resume'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^password-reset/$', password_reset,
        { 'post_reset_redirect': 'account:password_reset_done' },
        name = 'password_reset',
    ),
    url(r'^password-reset/done/$', password_reset_done,
        name='password_reset_done'
    ),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        { 'post_reset_redirect': 'account:password_reset_complete' },
        name='password_reset_confirm',
    ),
    url(r'^password-reset/complete/$', password_reset_complete,
        name='password_reset_complete'
    ),
]
