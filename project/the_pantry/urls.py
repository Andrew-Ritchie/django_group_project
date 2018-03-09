from django.conf.urls import url
from the_pantry import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^trending/', views.trending, name='trending'),
    url(r'^categories/', views.categories, name='categories'),
    # ADD SUBCATEGORIES
    url(r'^favourites/', views.favourites, name='favourites'),
    url(r'^profile/', views.profile, name='profile'),
    # ADD PROFILE/UPLOADS
    url(r'^latest/', views.latest, name='latest'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^publish/', views.publish, name='publish'),

    #===========================================#
    #    OTHER USER PROFILES  + LOGOUT          #
    #===========================================#

    # Should logout just take u to login or should it show a message first?

#    url(r'^logout/', views.logout, name='logout'),
]
