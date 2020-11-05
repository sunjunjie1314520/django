import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

django.setup()

from example import models

models.Comment.objects.create(
    news_id=1,
    content='@吕豪:你好呀',
    user_id=2,
    depth=2,
    reply_id=5
)
