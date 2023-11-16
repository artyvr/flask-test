""" Application tests """

import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    """ Basic tests """

    def test_index(self):
        """ Test index page """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        """ Test about page """
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_random(self):
        """ Test random page """
        tester = app.test_client(self)
        response = tester.get('/random', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
