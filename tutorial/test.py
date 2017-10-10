import unittest

from pyramid import testing


class TutorialViewTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home

        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Visit', response.body)

    def test_hello(self):
        from .views import hello

        request = testing.DummyRequest()
        response = hello(request)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Go Back', response.body)

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<body>Visit', res.body)

    def test_howdy(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<body>Go back', res.body)
