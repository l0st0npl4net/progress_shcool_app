from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestCoursesAppMethods(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')

    def test_index_page_view(self):
        response = self.client.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html')

    def test_about_us_view(self):
        response = self.client.get(reverse('courses:about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/about_us.html')

    def test_courses_view(self):
        response = self.client.get(reverse('courses:courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses_view.html')

    def test_lessons_view(self):
        response = self.client.get(reverse('courses:lessons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/lesson_view.html')
