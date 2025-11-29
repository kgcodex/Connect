# Backend File Structure

```
backend/
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── **init**.py
│   ├── management/
│   │   ├── commands/
│   │   │   ├── **init**.py
│   │   │   └── seed_db.py
│   │   ├── **init**.py
│   │   └── seed_data/
│   │   ├── posts/
│   │   │   ├── post1.jpeg
│   │   │   ├── post2.jpeg
│   │   │   ├── post3.jpeg
│   │   │   ├── post4.jpeg
│   │   │   └── post5.jpeg
│   │   └── profile_pics/
│   │   ├── face1.png
│   │   ├── face2.png
│   │   ├── face3.png
│   │   ├── face4.png
│   │   └── face5.png
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── **init**.py
│   ├── models.py
│   ├── serializers/
│   │   ├── auth_serializer.py
│   │   ├── comment_serializer.py
│   │   ├── follow_serializer.py
│   │   ├── **init**.py
│   │   ├── post_serializer.py
│   │   ├── search_serializer.py
│   │   └── user_serializer.py
│   ├── tests/
│   │   ├── base.py
│   │   ├── **init**.py
│   │   ├── routes.py
│   │   ├── test_auth.py
│   │   ├── test_comments.py
│   │   ├── test_feed.py
│   │   ├── test_follow.py
│   │   ├── test.png
│   │   ├── test_post.py
│   │   ├── test_search.py
│   │   ├── test_user_posts.py
│   │   └── test_user_profile.py
│   ├── utils/
│   │   ├── **init**.py
│   │   ├── rename_file.py
│   │   └── validate_age.py
│   └── v1/
│   ├── **init**.py
│   ├── urls.py
│   ├── views/
│   │   ├── auth_view.py
│   │   ├── comment_view.py
│   │   ├── feed_view.py
│   │   ├── follow_view.py
│   │   ├── **init**.py
│   │   ├── post_view.py
│   │   ├── profile_view.py
│   │   └── search_view.py
│   └── views**.py
├── connect_backend/
│   ├── asgi.py
│   ├── **init**.py
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   ├── **init\_\_.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── coverage.svg
├── Makefile
├── manage.py
├── pytest.ini
└── requirements.txt
```
