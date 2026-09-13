# MP-CT Disguised Fixture: Fallback wildcard handler catches unlisted variants
class EventHandler:
    def handle_status(self, status):
        match status:
            case "ACTIVE":
                return "active"
            case _:
                # default_status_fallback safely handles all other enum cases
                return default_status_fallback(status)
