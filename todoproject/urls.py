from django.conf.urls import include, url
from django.contrib import admin
from todoapp.views import todoView, addTodo, deleteTodo

urlpatterns = [
    # Examples:
    # url(r'^$', 'todoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/', todoView),
    url(r'^addTodo/', addTodo),
    url(r'^deleteTodo/(?P<todo_id>\w+)/', deleteTodo),
]


#url(r'^emailresend/(?P<id>\w+)/$', 'userapp.rummyauth.verificationemailresend', name='emailresend')