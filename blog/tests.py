from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls): # ravesh behtar
        cls.user = User.objects.create(username='user_m')
        cls.post1 = Post.objects.create(
            title='title_post1',
            text='this is the description test',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title='title_post2',
            text='this is test post2',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )

    # def setUp(self):
    #     self.user = User.objects.create(username='user_m')
    #     self.post1 = Post.objects.create(
    #         title='title_post1',
    #         text='this is the description test',
    #         status=Post.STATUS_CHOICES[0][0],
    #         author=self.user,
    #     )
    #     self.post2 = Post.objects.create(
    #         title='title_post2',
    #         text='this is test post2',
    #         status=Post.STATUS_CHOICES[1][0],
    #         author=self.user,
    #     )

    def test_post_model_srt(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'title_post1')
        self.assertEqual(self.post1.text, 'this is the description test')

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_posts_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[885]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'post3',
            'text': 'test post 3',
            'author': self.user.id,
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'post3')
        self.assertEqual(Post.objects.last().text, 'test post 3')


    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args=[self.post2.id]), {
            'title': 'title_post2 update',
            'text': 'this is the description test update',
            'author': self.post2.author.id,
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'title_post2 update')
        self.assertEqual(Post.objects.last().text, 'this is the description test update')


    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)

