# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import TEST_PASSWORD
from login.tests.model_maker import make_user


class SearchViewTest(TestCase):

    def setUp(self):
        self.user = make_user('ed')
        make_user('sam', is_staff=True)

    def test_search_not_logged_in(self):
        response = self.client.get(reverse('search.search'))
        self.assertEqual(response.status_code, 302)

    def test_search_normal_user_logged_in(self):
        # 'ed' is a normal user (not staff) so should NOT have access
        self.assertTrue(
            self.client.login(username='ed', password=TEST_PASSWORD)
        )
        response = self.client.get(reverse('search.search'))
        self.assertEqual(response.status_code, 403)

    def test_search_staff_user_logged_in(self):
        # 'sam' is a member of staff, so should be able to see the page
        self.assertTrue(
            self.client.login(username='sam', password=TEST_PASSWORD)
        )
        response = self.client.get(reverse('search.search'))
        self.assertEqual(response.status_code, 200)
