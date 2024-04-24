import requests 
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = ''

    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def createRepository(self, name):
        headers = {
            'Authorization': 'token ' + self.token,
            'Accept': 'application/vnd.github+json'
        }
        response = requests.post(self.api_url + '/user/repos', headers=headers, json={
            "name": name,
            "description": "Github api Test Repository",
            "homepage": "https://RukenAfsin.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True  
        })
        return response.json()

    def deleteRepository(self, owner, repo):
        headers = {
            'Authorization': 'token ' + self.token,
            'Accept': 'application/vnd.github+json'
        }
        response = requests.delete(f'{self.api_url}/repos/{owner}/{repo}', headers=headers)
        return response.status_code

github = Github()
while True:
    secim = input('1-Find User\n2- Get Repositories\n3- Create Repository\n4- Delete Repository\n5-Exit\n Seçim : ')

    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f'name: {result["name"]} public repos: {result["public_repos"]} follower: {result["followers"]}')
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(f' Repo Name: {repo["name"]}')
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        elif secim == '4':
            owner = input('repository owner: ')
            repo = input('repository name: ')
            status_code = github.deleteRepository(owner, repo)
            if status_code == 204:
                print(f'{repo} repository has been deleted successfully.')
            else:
                print(f'Error occurred while deleting {repo} repository. Status code: {status_code}')
        else:
            print('Yanlış bir seçim yaptınız')