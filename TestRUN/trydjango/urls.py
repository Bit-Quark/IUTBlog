from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import contact_view,about_view,trying_view,login_view,blog_view,podcast_view,research_view,literature_view,stories_view,opportunities_view,achievement_view,events_view



urlpatterns = [
    #path('',about_view,name="about"),
    path('trying/',trying_view,name="trying"),
    path('',home_view,name="home"),
    path('home/',home_view,name="home"),
    path('contact/',contact_view,name="contact"),
    path('about-us/',about_view,name="about-us" ),
    path('admin/', admin.site.urls),
    path('login/',login_view,name="login" ),
    path('blog/',blog_view,name="blog" ),
    path('podcast/',podcast_view,name="podcast" ),
    path('research/',research_view,name="research" ),
    path('stories_experiences/',stories_view,name="stories_experiences" ),
    path('literature/',literature_view,name="literature" ),
    path('events/',events_view,name="events" ),
    path('achievement/',achievement_view,name="achievement" ),
    path('opportunities/',opportunities_view,name="opportunities" )
    

]