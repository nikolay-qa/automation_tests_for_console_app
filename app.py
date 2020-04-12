from blog import Blog


MENU_PROMPT = """Enter:\n 'c' for creating blog,\n 'l' to list blogs,\n 'r' to read one,\n 'p' to create a post,\n 'q' to quit.\n"""
POST_TEMPLATE = "---{}---\n{}"

blogs = dict()  # blog_name: Blog Object


def menu():
    """
    Show the user the available blogs
    Let the user make a choice
    Do something with this choice
    Eventually exit
    """
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print(f'- {blog}')


def ask_create_blog():
    title = input('Enter your blog title: \n')
    author = input('Enter your name: \n')
    blogs[title] = Blog(title, author)


def ask_read_blog():
    asked_blog = input('Enter title of the blog that you want to read: \n').title()
    # if blogs.get(asked_blog):
    #     print(f'Your blog: {blogs[asked_blog]}')
    # else:
    #     print(f'Blog with title {asked_blog} is not present in the Database')
    print_posts(blogs[asked_blog])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(f"---{post.title}---\n{post.content}")


def ask_create_post():
    blog_name = input('Enter blog title you want to write post in: \n').title()
    post_title = input('Enter your post title: \n').title()
    post_content = input('Enter your post content: \n')
    blogs[blog_name].create_post(post_title, post_content)
