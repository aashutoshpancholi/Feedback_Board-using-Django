#from django.core.urlresolvers import reverse

#from django.contrib.auth.models import User

from django.urls import reverse
from django.urls import resolve
from django.test import TestCase

from ..views import board_topics, new_topic #home
from ..views import BoardListView
from ..models import Board, Topic, Post

#from ..forms import NewTopicForm
#from .views import new_topic



class HomeTests(TestCase):
    def setUp(self):        #def test_home_view_status_code(self):
        self.Board = Board.objects.create(name='Django', description='Django board.')  #self.board in REAL
        url = reverse('home')
        self.response = self.client.get(url)    #response = self.client.get(url)
        #self.assertEquals(response.status_code, 200)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        #self.assertEquals(view.func, home)
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.Board.pk})  #1 #kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
