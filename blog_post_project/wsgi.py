import os
from django.core.wsgi import get_wsgi_application

# Replace 'BLOG_PROJECT.settings' with your actual project folder name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_post_project.settings")

application = get_wsgi_application()
