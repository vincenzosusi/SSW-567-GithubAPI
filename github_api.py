import requests


def list_repositories(user_id):
    """
    Gets a list of repositories and the number of commits for a given Github user

    :param user_id: username of github user
    :return: list of pairs [repo name, num of commits]
    """
    res = requests.get('https://api.github.com/users/' + user_id + '/repos').json()
    if not isinstance(res, list):
        if res['message'] == "Not found":
            return "User not found"
        return "Invalid response from API"

    results = []  # used for testing
    for repo in res:
        commits = requests.get(
            'https://api.github.com/repos/' + user_id + '/' + repo['name'] + '/commits').json()
        results.append([repo['name'], len(commits)])
    return results


def print_results(repo_list):
    """
    Formats the list of repositories for printing to the console
    """
    for pair in repo_list:
        print('Repo: ' + pair[0] + ' Number of commits: ' + pair[1])


if __name__ == 'main':
    result_list = list_repositories('richkempinski')
    print_results(result_list)
