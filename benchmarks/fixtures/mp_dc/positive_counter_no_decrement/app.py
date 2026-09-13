# MP-DC Positive Fixture: Denormalized counter incremented on create but not decremented on delete
class PostService:
    def create_post(self, user_id, title):
        db.query("INSERT INTO posts (user_id, title) VALUES (%s, %s)", user_id, title)
        db.query("UPDATE users SET posts_count = posts_count + 1 WHERE id = %s", user_id)

    def delete_post(self, post_id, user_id):
        db.query("DELETE FROM posts WHERE id = %s", post_id)
        # NOTE: Missing posts_count decrement!
