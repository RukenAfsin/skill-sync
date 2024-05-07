import pytest
from github import Github

# Test için bir GitHub örneği oluşturalım
@pytest.fixture
def github():
    return Github()

# Birim test: getUser metodunu test etme
def test_getUser(github):
    result = github.getUser('RukenAfsin')
    assert result['name'] == 'Ruken Afsin'
    assert result['public_repos'] > 0
    assert result['followers'] > 0

# Birim test: getRepositories metodunu test etme
def test_getRepositories(github):
    result = github.getRepositories('RukenAfsin')
    assert len(result) > 0

# Birim test: createRepository metodunu test etme
def test_createRepository(github):
    result = github.createRepository('test-repo')
    assert 'name' in result and result['name'] == 'test-repo'

# Entegrasyon testi: API ile bağlantıyı test etme
def test_apiConnection():
    github = Github()
    assert github.getUser('RukenAfsin')
    assert github.getRepositories('RukenAfsin')

# Entegrasyon testi: createRepository ve deleteRepository metodlarını test etme
def test_createAndDeleteRepository(github):
    # Depo oluştur
    repo_name = 'test-repo'
    github.createRepository(repo_name)

    # Depo var mı kontrol et
    result = github.getRepositories('RukenAfsin')
    repo_names = [repo['name'] for repo in result]
    assert repo_name in repo_names

    # Depoyu sil
    github.deleteRepository('RukenAfsin', repo_name)

    # Depo silinmiş mi kontrol et
    result = github.getRepositories('RukenAfsin')
    repo_names = [repo['name'] for repo in result]
    assert repo_name not in repo_names
