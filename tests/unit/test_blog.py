from blog import Blog


def test_create_blog():
    b = Blog('Test', 'Test Author')
    assert 'Test' == b.title
    assert 'Test Author' == b.author
    assert [] == b.posts


def test_repr():
    b = Blog('Test', 'Test Author')
    b2 = Blog('My Day', 'Rolf')
    assert b.__repr__() == 'Test by Test Author(0 posts)'
    assert b2.__repr__() == 'My Day by Rolf(0 posts)'


def test_repr_multiple_posts():
    b = Blog('Test', 'Test Author')
    b.posts = ['test1', 'test2']
    b2 = Blog('My Day', 'Rolf')
    b2.posts = ['test1']
    assert b.__repr__() == 'Test by Test Author(2 posts)'
    assert b2.__repr__() == 'My Day by Rolf(1 post)'
