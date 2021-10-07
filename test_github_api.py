import unittest
from unittest.mock import Mock, patch

from github_api import list_repositories


class TestGithubApi(unittest.TestCase):

    @patch('github_api.requests.get')
    def test_invalid_user(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = {
            'message': "Not found"
        }
        response = list_repositories('InvalidUserNameForGithub')
        self.assertEqual("User not found", response)

    @patch('github_api.requests.get')
    def test_return_not_ok(self, mock_get):
        mock_get.return_value.ok = False
        response = list_repositories('testUser')
        self.assertEqual("Invalid response from API", response)

    @patch('github_api.requests.get')
    def test_correct_output(self, mock_get):
        repo_list = [
            {'name': "test_repo1"},
            {'name': "test_repo2"}
        ]
        commit_list_1 = [
            {'node_id': 'NDKSJHMDKNSUHDH'},
            {'node_id': 'kshdahoedaenodeno'}
        ]
        commit_list_2 = [
            {'node_id': 'NDKSJHMDKNSUHDH'}
        ]
        mock_get.return_value.ok = True
        mock_get.return_value.json.side_effect = [repo_list, commit_list_1, commit_list_2]
        response = list_repositories('testUser')
        self.assertEqual([['test_repo1', 2], ['test_repo2', 1]], response)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
