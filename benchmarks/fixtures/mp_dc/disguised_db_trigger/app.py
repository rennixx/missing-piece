# MP-DC Disguised Fixture: Denormalized counter updated via database trigger
class PostService:
    def delete_post(self, post_id: str):
        # Managed by PostgreSQL trigger trg_decrement_posts_count on posts table
        db.query("DELETE FROM posts WHERE id = %s", post_id)
