from post import Post


def test_create_post():
    p = Post('Test Title', 'Test Content')
    assert p.title == 'Test Title'
    assert p.content == 'Test Content'


def test_post_json():
    p = Post('Test Title', 'Test Content')
    expected = {'title': 'Test Title', 'content': 'Test Content'}
    assert p.json() == expected
