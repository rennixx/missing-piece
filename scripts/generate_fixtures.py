#!/usr/bin/env python3
"""
generate_fixtures.py

Generates positive, negative, exception, and disguised fixture repositories
for all benchmark scenarios defined in benchmarks/manifest.json.
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BENCHMARK_MANIFEST = ROOT_DIR / "benchmarks" / "manifest.json"

FIXTURE_CONTENTS = {
    # MP-LC
    "lc_upload_no_delete": {
        "app.py": '''# MP-LC Positive Fixture: Upload without Delete/Cleanup
import os

class StorageService:
    def upload_user_avatar(self, user_id: str, file_data: bytes) -> str:
        """Uploads avatar file to persistent S3 bucket."""
        key = f"avatars/{user_id}.png"
        print(f"Uploaded {key}")
        return key

    # NOTE: Missing delete_user_avatar or purge_avatar cleanup function!
'''
    },
    "lc_upload_with_delete": {
        "app.py": '''# MP-LC Negative Fixture: Upload WITH Delete
class StorageService:
    def upload_user_avatar(self, user_id: str, file_data: bytes) -> str:
        key = f"avatars/{user_id}.png"
        print(f"Uploaded {key}")
        return key

    def delete_user_avatar(self, user_id: str) -> None:
        """Deletes user avatar file from persistent storage."""
        key = f"avatars/{user_id}.png"
        print(f"Deleted {key}")
'''
    },
    "lc_immutable_audit_log": {
        "app.py": '''# MP-LC Exception Fixture: Append-Only Immutable Audit Log
class AuditLogger:
    """Immutable append-only security log table. Intentionally no delete path."""
    def log_security_event(self, event_type: str, actor_id: str):
        print(f"AUDIT_RECORD: {event_type} by {actor_id}")
'''
    },
    "lc_disguised_cleanup": {
        "app.py": '''# MP-LC Disguised Fixture: Non-standard naming for asset deletion
class StorageManager:
    def store_asset(self, asset_id: str):
        print(f"Stored {asset_id}")

    def purge_stale_assets(self, age_days: int = 30):
        """Asynchronously cleans up expired asset files."""
        print(f"Purged assets older than {age_days} days")
'''
    },

    # MP-ST
    "st_pending_no_timeout": {
        "app.py": '''# MP-ST Positive Fixture: Pending order state with no timeout path
class OrderStatus:
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"

class OrderService:
    def create_order(self, cart_id: str) -> str:
        return OrderStatus.PENDING

    def mark_paid(self, order_id: str):
        # Transitions PENDING -> PAID
        pass

    # NOTE: Missing timeout transition or background expire_pending_orders sweep!
'''
    },
    "st_pending_with_timeout": {
        "app.py": '''# MP-ST Negative Fixture: Pending order state WITH timeout worker
class OrderStatus:
    PENDING = "pending"
    PAID = "paid"
    EXPIRED = "expired"

class OrderService:
    def create_order(self, cart_id: str) -> str:
        return OrderStatus.PENDING

    def mark_paid(self, order_id: str):
        pass

    def expire_stale_orders(self):
        """Cron job transition PENDING -> EXPIRED after 15 minutes."""
        print("Expired stale pending orders")
'''
    },
    "st_terminal_cancelled_no_timeout": {
        "app.py": '''# MP-ST Exception Fixture: Terminal cancelled state with no timeout transition
class OrderStatus:
    CANCELLED = "cancelled"

class OrderService:
    def close_order(self, order_id: str):
        # Terminal state intentionally has no further transitions
        return OrderStatus.CANCELLED
'''
    },

    # MP-SY
    "sy_grant_no_revoke": {
        "app.py": '''# MP-SY Positive Fixture: grant_role without revoke_role
class PermissionManager:
    def grant_role(self, user_id: str, role_name: str):
        print(f"Granted {role_name} to {user_id}")

    # NOTE: Missing revoke_role counterpart!
'''
    },
    "sy_grant_and_revoke": {
        "app.py": '''# MP-SY Negative Fixture: grant_role WITH revoke_role
class PermissionManager:
    def grant_role(self, user_id: str, role_name: str):
        print(f"Granted {role_name} to {user_id}")

    def revoke_role(self, user_id: str, role_name: str):
        print(f"Revoked {role_name} from {user_id}")
'''
    },
    "sy_one_way_hash_token": {
        "app.py": '''# MP-SY Exception Fixture: One-way hash intentionally has no decrypt counterpart
import hashlib

class TokenService:
    def hash_token(self, raw_token: str) -> str:
        # One-way cryptographic hash intentionally irreversible
        return hashlib.sha256(raw_token.encode()).hexdigest()
'''
    },

    # MP-MG
    "mg_admin_no_auth": {
        "app.py": '''# MP-MG Positive Fixture: Sensitive admin mutation without authorization
from flask import Flask, request

app = Flask(__name__)

@app.route("/admin/users/<user_id>", methods=["DELETE"])
def perform_user_purge(user_id):
    # NOTE: Mutates production DB without @require_auth or permission check!
    return f"Purged user {user_id}", 200
'''
    },
    "mg_admin_with_auth": {
        "app.py": '''# MP-MG Negative Fixture: Admin mutation WITH authorization guard
from flask import Flask, request

app = Flask(__name__)

def require_admin(func):
    def wrapper(*args, **kwargs):
        if not request.headers.get("X-Admin-Token"):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

@app.route("/admin/users/<user_id>", methods=["DELETE"])
@require_admin
def perform_user_purge(user_id):
    return f"Purged user {user_id}", 200
'''
    },
    "mg_public_registration": {
        "app.py": '''# MP-MG Exception Fixture: Public signup endpoint without auth guard
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/register", methods=["POST"])
def register_user():
    # Public registration endpoint intentionally unauthenticated
    data = request.get_json()
    return {"status": "created", "user": data.get("username")}, 201
'''
    },

    # MP-SE
    "se_cancel_no_inventory": {
        "app.py": '''# MP-SE Positive Fixture: Order cancellation missing inventory release
class OrderController:
    def cancel_order(self, order_id: str):
        order = self.db.get(order_id)
        order.status = "CANCELLED"
        self.db.save(order)
        # NOTE: Missing inventory restoration side-effect!
'''
    },
    "se_cancel_with_inventory": {
        "app.py": '''# MP-SE Negative Fixture: Order cancellation WITH inventory release
class OrderController:
    def cancel_order(self, order_id: str):
        order = self.db.get(order_id)
        order.status = "CANCELLED"
        self.db.save(order)
        self.inventory_service.unreserve_items(order.items)
'''
    },
    "se_disguised_inventory_event": {
        "app.py": '''# MP-SE Disguised Fixture: Inventory release handled via domain event bus
class OrderService:
    def cancel_order(self, order_id: str):
        # Disguised counterpart: triggers inventory replenishment via event bus
        emit_event(DomainEvent.ORDER_VOIDED, {"order_id": order_id})
'''
    },

    # MP-FR
    "fr_webhook_no_idempotency": {
        "app.py": '''# MP-FR Positive Fixture: Webhook receiver without idempotency
@app.route("/webhooks/stripe", methods=["POST"])
def handle_stripe_webhook():
    data = request.get_json()
    # NOTE: Processes payment event directly without checking idempotency key or event_id deduplication!
    process_payment(data["amount"])
    return "OK", 200
'''
    },
    "fr_webhook_with_idempotency": {
        "app.py": '''# MP-FR Negative Fixture: Webhook receiver WITH idempotency check
@app.route("/webhooks/stripe", methods=["POST"])
def handle_stripe_webhook():
    data = request.get_json()
    event_id = data["id"]
    if db.processed_events.find_one({"event_id": event_id}):
        return "Already processed", 200
    process_payment(data["amount"])
    db.processed_events.insert({"event_id": event_id})
    return "OK", 200
'''
    },
    "fr_idempotent_get_endpoint": {
        "app.py": '''# MP-FR Exception Fixture: Read endpoint naturally idempotent without tokens
from flask import Flask

app = Flask(__name__)

@app.route("/api/reports/<report_id>", methods=["GET"])
def get_report(report_id):
    # HTTP GET is naturally idempotent without idempotency key checks
    return {"report_id": report_id, "data": "ready"}, 200
'''
    },

    # MP-OC
    "oc_user_delete_orphans": {
        "app.py": '''# MP-OC Positive Fixture: User deletion leaves orphaned uploads
class AccountManager:
    def delete_account(self, user_id: str):
        db.query("DELETE FROM users WHERE id = %s", user_id)
        # NOTE: UserUploads table records and S3 objects left orphaned!
'''
    },
    "oc_user_delete_cascades": {
        "app.py": '''# MP-OC Negative Fixture: User deletion cascades to user uploads
class AccountManager:
    def delete_account(self, user_id: str):
        db.query("DELETE FROM user_uploads WHERE user_id = %s", user_id)
        db.query("DELETE FROM users WHERE id = %s", user_id)
'''
    },
    "oc_shared_system_tag": {
        "app.py": '''# MP-OC Exception Fixture: Shared reference tag retained on project delete
class ProjectService:
    def delete_project(self, project_id: str):
        # Shared global resource intentionally not deleted during project removal
        db.query("DELETE FROM projects WHERE id = %s", project_id)
'''
    },

    # MP-AU
    "au_new_endpoint_unprotected": {
        "app.py": '''# MP-AU Positive Fixture: New route omitted from RBAC policy matrix
ROUTER = {
    "/api/dashboard": "read",
    "/api/settings": "write",
    "/api/export_data": None # NOTE: Unprotected endpoint!
}
'''
    },
    "au_new_endpoint_protected": {
        "app.py": '''# MP-AU Negative Fixture: Endpoint registered in RBAC policy
ROUTER = {
    "/api/dashboard": "read",
    "/api/settings": "write",
    "/api/export_data": "admin"
}
'''
    },
    "au_health_check_public": {
        "app.py": '''# MP-AU Exception Fixture: Public health check route
ROUTER = {
    "/api/dashboard": "read",
    "/healthz": None # Uptime probe intentionally public
}
'''
    },

    # MP-AS
    "as_producer_no_recovery": {
        "app.py": '''# MP-AS Positive Fixture: Async queue job without dead-letter recovery
class JobWorker:
    def process_job(self, job_data):
        # NOTE: If exception occurs, job is dropped without retry limit or dead-letter queue!
        do_work(job_data)
'''
    },
    "as_producer_with_recovery": {
        "app.py": '''# MP-AS Negative Fixture: Async queue job WITH retry limit and DLQ
class JobWorker:
    def process_job(self, job_data):
        try:
            do_work(job_data)
        except Exception as e:
            if job_data.retries >= 3:
                self.dead_letter_queue.push(job_data, str(e))
            else:
                self.retry_queue.push(job_data)
'''
    },
    "as_disguised_worker_retry": {
        "app.py": '''# MP-AS Disguised Fixture: Queue retries handled by cloud infrastructure
class WorkerService:
    def consume_message(self, message):
        # AWS SQS RedrivePolicy managed externally via Terraform infrastructure
        process_payload(message.body)
'''
    },

    # MP-OP
    "op_env_missing_config": {
        "app.py": '''# MP-OP Positive Fixture: Env var used in code missing from config validation
import os
analytics_url = os.environ["ANALYTICS_DB_URL"] # NOTE: Missing from config schema or .env.example!
'''
    },
    "op_env_validated_config": {
        "app.py": '''# MP-OP Negative Fixture: Env var declared in config validation
import os

REQUIRED_CONFIG = ["ANALYTICS_DB_URL"]

def validate_config():
    for key in REQUIRED_CONFIG:
        assert key in os.environ, f"Missing required env var: {key}"
'''
    },
    "op_disguised_env_provider": {
        "app.py": '''# MP-OP Disguised Fixture: Config fetched dynamically from secret manager
class ConfigService:
    def get_database_credentials(self):
        # Disguised config provider: vault_client.get_secret retrieves dynamic creds
        return vault_client.get_secret("db_credentials")
'''
    },

    # MP-DC
    "dc_counter_no_decrement": {
        "app.py": '''# MP-DC Positive Fixture: Denormalized counter incremented on create but not decremented on delete
class PostService:
    def create_post(self, user_id, title):
        db.query("INSERT INTO posts (user_id, title) VALUES (%s, %s)", user_id, title)
        db.query("UPDATE users SET posts_count = posts_count + 1 WHERE id = %s", user_id)

    def delete_post(self, post_id, user_id):
        db.query("DELETE FROM posts WHERE id = %s", post_id)
        # NOTE: Missing posts_count decrement!
'''
    },
    "dc_counter_with_decrement": {
        "app.py": '''# MP-DC Negative Fixture: Counter updated on create AND delete
class PostService:
    def create_post(self, user_id, title):
        db.query("INSERT INTO posts (user_id, title) VALUES (%s, %s)", user_id, title)
        db.query("UPDATE users SET posts_count = posts_count + 1 WHERE id = %s", user_id)

    def delete_post(self, post_id, user_id):
        db.query("DELETE FROM posts WHERE id = %s", post_id)
        db.query("UPDATE users SET posts_count = posts_count - 1 WHERE id = %s", user_id)
'''
    },
    "dc_disguised_db_trigger": {
        "app.py": '''# MP-DC Disguised Fixture: Denormalized counter updated via database trigger
class PostService:
    def delete_post(self, post_id: str):
        # Managed by PostgreSQL trigger trg_decrement_posts_count on posts table
        db.query("DELETE FROM posts WHERE id = %s", post_id)
'''
    },

    # MP-CT
    "ct_enum_unhandled": {
        "app.py": '''# MP-CT Positive Fixture: Enum value unhandled in handler
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REFUNDED = "refunded"

def handle_payment_status(status: PaymentStatus):
    if status == PaymentStatus.PENDING:
        print("Pending")
    elif status == PaymentStatus.COMPLETED:
        print("Completed")
    # NOTE: Missing handling for PaymentStatus.REFUNDED!
'''
    },
    "ct_enum_handled": {
        "app.py": '''# MP-CT Negative Fixture: All Enum values handled
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REFUNDED = "refunded"

def handle_payment_status(status: PaymentStatus):
    if status == PaymentStatus.PENDING:
        print("Pending")
    elif status == PaymentStatus.COMPLETED:
        print("Completed")
    elif status == PaymentStatus.REFUNDED:
        print("Refunded")
'''
    },
    "ct_disguised_wildcard_handler": {
        "app.py": '''# MP-CT Disguised Fixture: Fallback wildcard handler catches unlisted variants
class EventHandler:
    def handle_status(self, status):
        match status:
            case "ACTIVE":
                return "active"
            case _:
                # default_status_fallback safely handles all other enum cases
                return default_status_fallback(status)
'''
    },

    # MP-CF
    "cf_optional_integration_crash": {
        "app.py": '''# MP-CF Positive Fixture: Optional integration crashes when key is missing
import os

# NOTE: Unconditional access crashes app if optional SLACK_WEBHOOK_URL is not set
slack_url = os.environ["SLACK_WEBHOOK_URL"]
'''
    },
    "cf_optional_integration_fallback": {
        "app.py": '''# MP-CF Negative Fixture: Safe fallback for optional integration
import os

slack_url = os.environ.get("SLACK_WEBHOOK_URL", None)

def notify_slack(msg):
    if not slack_url:
        print("Slack notification skipped (SLACK_WEBHOOK_URL not configured)")
        return
    print(f"Sent to Slack: {msg}")
'''
    },
    "cf_disguised_cloud_config": {
        "app.py": '''# MP-CF Disguised Fixture: Integration config loaded via dynamic cloud provider
class IntegrationConfig:
    def get_slack_url(self):
        # cloud_config_provider.get_default supplies fallback integration URL
        return cloud_config_provider.get_default("SLACK_WEBHOOK_URL")
'''
    },

    # MP-OB
    "ob_unmonitored_settlement_failure": {
        "app.py": '''# MP-OB Positive Fixture: Unmonitored settlement failure
class SettlementService:
    def process_batch_settlement(self, transactions):
        for tx in transactions:
            try:
                self.settle_transaction(tx)
            except Exception as e:
                # NOTE: Missing terminal failure alert, metric, or dead-letter observability!
                pass

    def settle_transaction(self, tx):
        pass
'''
    },
    "ob_monitored_settlement_failure": {
        "app.py": '''# MP-OB Negative Fixture: Monitored settlement failure with alert and metric
class SettlementService:
    def process_batch_settlement(self, transactions):
        for tx in transactions:
            try:
                self.settle_transaction(tx)
            except Exception as e:
                # Disproof counterpart: Emits terminal failure alert and records metric
                self.alert_channel.notify(f"Settlement failed for tx {tx.id}: {e}")
                self.metrics.record_settlement_failure(tx.id)

    def settle_transaction(self, tx):
        pass
'''
    },
    "ob_disguised_apm_auto_instrumentation": {
        "app.py": '''# MP-OB Disguised Fixture: APM auto-instrumentation catches errors
class SettlementProcessor:
    # ddtrace.tracer.wrap automatically records traces and unhandled error metrics
    def process_settlement(self, tx):
        pass
'''
    }
}

def main():
    print("=== Generating Benchmark Fixture Repositories ===")
    with open(BENCHMARK_MANIFEST, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    created_count = 0
    for scenario in manifest["scenarios"]:
        scenario_id = scenario["id"]
        fixture_rel_path = scenario["path"]
        target_dir = ROOT_DIR / fixture_rel_path
        target_dir.mkdir(parents=True, exist_ok=True)

        files = FIXTURE_CONTENTS.get(scenario_id, {
            "app.py": f"# Fixture for scenario {scenario_id}\n"
        })

        for filename, content in files.items():
            file_path = target_dir / filename
            file_path.write_text(content.strip() + "\n", encoding="utf-8")
            created_count += 1

    print(f"[OK] Generated {created_count} fixture file(s) across {len(manifest['scenarios'])} scenarios.")

if __name__ == "__main__":
    main()
