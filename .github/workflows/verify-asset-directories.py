from pathlib import Path
import re


posts = []
for directory in Path("assets").iterdir():
    if directory.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}-", directory.name):
        post = Path("_posts", directory.name).with_suffix(".md")
        if not post.is_file():
            raise ValueError(f"missing post: {post}")
        posts.append(post)

print(f"discovered {len(posts)} asset directories for posts")
