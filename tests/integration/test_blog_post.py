from blog import Blog


def test_create_post_in_blog():
    b = Blog('Test', 'Test Author')
    b.create_post('Test Post', 'Test Content')
    assert len(b.posts) == 1
    assert b.posts[0].title == 'Test Post', f'{b.posts}'
    assert b.posts[0].content == 'Test Content'


def test_json_no_post():
    b = Blog('Test', 'Test Author')
    expected_no_post = {'title': 'Test',
                        'author': 'Test Author',
                        'posts': []}
    assert b.json() == expected_no_post


def test_blog_json():
    b = Blog('Test', 'Test Author')
    b.create_post('Test Post', 'Test Content')
    expected = {'title': 'Test',
                'author': 'Test Author',
                'posts': [
                    {
                        'title': 'Test Post',
                        'content': 'Test Content'
                    }
                ]
                }
    assert b.json() == expected
