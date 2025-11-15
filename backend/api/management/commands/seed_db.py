import random
from pathlib import Path

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction
from faker import Faker

from api.models import Comment, Follow, Like, Post, User

# Configurable parameters
NUM_USERS = 100
MAX_POSTS_PER_USER = 5
MAX_COMMENTS_PER_POST = 10
MAX_FOLLOWS_PER_USER = 60


class Command(BaseCommand):
    """
    Seed the database with sample data for testing and development."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()
        self.users = []
        self.posts = []

        # Profile pics
        base_dir = Path(__file__).resolve().parent.parent
        self.profile_pic_dir = base_dir / "seed_data" / "profile_pics"
        self.profile_pics = [
            "face1.png",
            "face2.png",
            "face3.png",
            "face4.png",
            "face5.png",
        ]

        # Posts
        self.posts_dir = base_dir / "seed_data" / "posts"
        self.post_files = [
            "post1.jpeg",
            "post2.jpeg",
            "post3.jpeg",
            "post4.jpeg",
            "post5.jpeg",
        ]

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(" > Seeding database..."))

        # Clear existing data
        Follow.objects.all().delete()
        Comment.objects.all().delete()
        Like.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
        self.stdout.write(" + Old data deleted.")

        # Create Users
        self.stdout.write(self.style.SUCCESS(f" > Creating {NUM_USERS} users..."))
        for _ in range(NUM_USERS):
            try:
                user = User.objects.create_user(
                    email=self.fake.email(),
                    username=self.fake.user_name(),
                    name=self.fake.name(),
                    password="password123",
                    dob=self.fake.date_of_birth(minimum_age=18, maximum_age=80),
                    bio=self.fake.text(max_nb_chars=250),
                )
                # Assign a random profile picture
                pic_name = random.choice(self.profile_pics)
                pic_path = self.profile_pic_dir / pic_name

                with open(pic_path, "rb") as f:
                    pic_content = ContentFile(f.read(), name=pic_name)
                    user.profile_pic.save(pic_name, pic_content, save=True)

                self.users.append(user)

            except IntegrityError:
                self.stdout.write(
                    self.style.WARNING(
                        "Could not create user. Duplicate email or username. Skipping."
                    )
                )
                continue

        self.stdout.write(f" + {len(self.users)} users created.")

        # Create Follows
        self.stdout.write(self.style.SUCCESS(" > Creating follow relationships..."))

        follows_row = []

        for user in self.users:
            num_follows = random.randint(10, MAX_FOLLOWS_PER_USER)
            other_users = [u for u in self.users if u != user]

            if num_follows > len(other_users):
                num_follows = len(other_users)

            users_to_follow = random.sample(other_users, num_follows)

            for followee in users_to_follow:
                follows_row.append(Follow(user=followee, follower=user))

        Follow.objects.bulk_create(follows_row)
        self.stdout.write(f" + {len(follows_row)} follow relationships created.")

        # Create Posts
        self.stdout.write(self.style.SUCCESS(" > Creating Posts..."))

        for user in self.users:
            num_posts = random.randint(0, MAX_POSTS_PER_USER)
            for _ in range(num_posts):
                post = Post.objects.create(
                    user=user, content=self.fake.text(max_nb_chars=250)
                )

                post_image_name = random.choice(self.post_files)
                post_image_path = self.posts_dir / post_image_name

                try:
                    with open(post_image_path, "rb") as f:
                        pic_content = ContentFile(f.read(), name=post_image_name)
                        post.media_url.save(post_image_name, pic_content, save=True)

                except FileNotFoundError:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Could not find post image: {post_image_path}. Skipping."
                        )
                    )
                    continue

                self.posts.append(post)

        self.stdout.write(f" + {len(self.posts)} posts created.")

        # Create Likes
        self.stdout.write(self.style.SUCCESS(" > Creating likes..."))

        if not self.posts:
            self.stdout.write(self.style.WARNING("No posts exist, skipping likes."))
        else:
            likes_to_create = []
            for post in self.posts:
                likes_to_create.append(
                    Like(post=post, count=random.randint(0, len(self.users)))
                )

            Like.objects.bulk_create(likes_to_create)

        self.stdout.write(f" + {len(likes_to_create)} like records created.")

        # Create Comments
        self.stdout.write(self.style.SUCCESS(" > Creating comments..."))

        if not self.posts:
            self.stdout.write(self.style.WARNING("No posts exist, skipping comments."))
        else:
            comments_to_create = []
            for post in self.posts:
                num_comments = random.randint(0, MAX_COMMENTS_PER_POST)

                for _ in range(num_comments):
                    comments_to_create.append(
                        Comment(
                            post=post,
                            user=random.choice(self.users),  # Any user can comment
                            content=self.fake.sentence(
                                nb_words=10
                            ),  # 10-word fake sentence
                        )
                    )

            Comment.objects.bulk_create(comments_to_create)
            self.stdout.write(f" + {len(comments_to_create)} comments created.")

        self.stdout.write(self.style.SUCCESS(" > Database seeding complete."))
