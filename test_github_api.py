import unittest

from github_api import list_repositories


class TestGithubApi(unittest.TestCase):

    def test_invalid_user(self):
        self.assertEqual("User not found", list_repositories('InvalidUserName'))

    def test_correct_output(self):
        self.assertEqual(
            [
                ['csp', 2],
                ['hellogitworld', 30],
                ['helloworld', 6],
                ['Mocks', 10],
                ['Project1', 2],
                ['richkempinski.github.io', 9],
                ['threads-of-life', 1],
                ['try_nbdev', 2],
                ['try_nbdev2', 5]
            ], list_repositories('richkempinski'))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
