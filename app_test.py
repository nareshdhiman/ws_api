import os
import app
import unittest
import tempfile
import redis

class CounterTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        with app.app.app_context():
            self.r = app.init_db()

    def tearDown(self):
        self.r.flushdb()

    def test_count(self):
        self.app.get("/key/test")
        val = self.r.get("test")
        self.assertEquals(val, "1", "key didn't increment")

    def test_reset(self):
        self.app.get("/key/test")
        self.app.post("/_reset")
        val = self.r.get("test")
        self.assertIs(val, None, "db didn't flush")


if __name__ == '__main__':
    unittest.main()
