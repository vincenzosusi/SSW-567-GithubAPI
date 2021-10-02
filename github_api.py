import requests

def list_repositories(userId):

    r = requests.get('https://api.github.com/users/' + userId + '/repos').json()
    if (r == []):
        return "User not found"
    results = []  # used for testing
    for repo in r:
        commits = requests.get('https://api.github.com/repos/' + userId + '/' + repo['name'] + '/commits').json()
        results.append([repo['name'], len(commits)])
    return results

def print_results(l):
    for pair in l:
        print('Repo: ' + pair[0] + ' Number of commits: ' + pair[1])


if __name__ == 'main':
    result_list = list_repositories('richkempinski')
    print_results(result_list)
