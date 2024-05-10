import pytest
from instagram import Instagram



@pytest.fixture
def instagram():
    return Instagram()

# def test_sign_in(instagram):
#     instagram.sign_in()
#     assert instagram.browser.current_url == 'https://www.instagram.com/'

# def test_search(instagram):
#     instagram.search('berat')
#     assert 'berat' in instagram.browser.page_source

# def test_followUser(instagram):
#     instagram.followUser('beratt.afsin')
#     assert 'Kullanıcı takip edildi.' in instagram.browser.page_source

# def test_sign_in_false(instagram):
#     instagram.sign_in_false()
#     assert 'Hata' in instagram.browser.page_source


# def test_validate(instagram):
#    assert instagram.validate_email("example@example.com") == True



def test_logout(instagram):
    instagram.logout()
    assert instagram.browser.current_url == 'https://www.instagram.com/'
