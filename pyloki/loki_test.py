import unittest
from .loki import PyLoki


class PyLokiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = PyLoki(source='PyLoki Test', job='testing')

    def test_info_message(self):
        r = self.client.info('Testing info')
        self.assertEqual(r.status_code, 204, 'Status to be 204')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.info('PyLoki test exited')


if __name__ == '__main__':
    unittest.main()
