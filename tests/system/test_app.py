import app
from blog import Blog
from post import Post
from unittest.mock import patch


def test_menu_create_blog():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
        app.menu()
        assert app.blogs.get('Test Create Blog', 'fail') != 'fail'


def test_menu_print_blogs():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ('l', 'q')
        with patch('app.print_blogs') as mocked_print_blogs:
            app.menu()
            # assert mocked_print_blogs.call_count == 2  #  checking that print_blogs() function called twice
            mocked_print_blogs.call.second()


def test_menu_ask_read_blog():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ('r', 'q')
        with patch('app.ask_read_blog') as mocked_ask_read_blog:
            app.menu()
            mocked_ask_read_blog.assert_called_once()


def test_menu_ask_create_post():
    with patch('builtins.input', side_effect=['p', 'q']):
        with patch('app.ask_create_post') as mocked_ask_create_post:
            app.menu()
            mocked_ask_create_post.assert_called_once()


def test_menu_quit():
    with patch('app.print_blogs') as mocked_print_blogs:
        with patch('builtins.input', return_value='q'):
            app.menu()
            mocked_print_blogs.assert_called_once()


def test_menu_prints_prompt():
    with patch('builtins.input', return_value='q') as mocked_input:
        app.menu()
        mocked_input.assert_called_with(app.MENU_PROMPT)


def test_menu_calls_prints_blogs():
    with patch('app.print_blogs') as mocked_print_blogs:
        with patch('builtins.input', return_value='q'):
            app.menu()
            mocked_print_blogs.assert_called()


def test_print_blogs():
    blog = Blog('Test', 'Test Author')
    app.blogs = {'Test': blog}
    with patch('builtins.print') as mocked_print:
        app.print_blogs()
        mocked_print.assert_called_with('- Test by Test Author(0 posts)')


def test_ask_create_blog():
    with patch('builtins.input', side_effect=['Test', 'Test Name']):
        app.ask_create_blog()
        assert app.blogs.get('Test', 'fail') != 'fail'


def test_ask_read_blog():
    blog = Blog('Test', 'Test Author')
    app.blogs = {'Test': blog}
    with patch('builtins.input', return_value='Test'):
        with patch('app.print_posts') as mocked_print_posts:
            app.ask_read_blog()
            mocked_print_posts.assert_called_with(blog)


def test_print_posts():
    blog = Blog('Test', 'Test Author')
    blog.create_post('Test Post', 'Test Content')
    app.blogs = {'Test': blog}
    with patch('app.print_post') as mocked_print_post:
        app.print_posts(blog)
        mocked_print_post.assert_called_with(blog.posts[0])


def test_print_post():
    post = Post('Test Post', 'Test Content')
    with patch('builtins.print') as mocked_print:
        app.print_post(post)
        expected = "---Test Post---\nTest Content"
        mocked_print.assert_called_with(expected)


def test_ask_create_post():
    blog = Blog('Test', 'Test Author')
    app.blogs = {'Test': blog}
    with patch('builtins.input', side_effect=['Test', 'Test Post Title', 'Test Post Content']):
        app.ask_create_post()
        assert blog.posts[0].title == 'Test Post Title'
        assert blog.posts[0].content == 'Test Post Content'
