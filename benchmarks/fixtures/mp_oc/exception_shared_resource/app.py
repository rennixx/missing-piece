# MP-OC Exception Fixture: Shared reference tag retained on project delete
class ProjectService:
    def delete_project(self, project_id: str):
        # Shared global resource intentionally not deleted during project removal
        db.query("DELETE FROM projects WHERE id = %s", project_id)
