# Security and Permission Completeness

This is not a vulnerability scanner. Only inspect security behavior that is implied by observed operations/trust boundaries.

## Authorization mapping

When a privileged mutation is found:
- locate enforcement mechanism;
- compare adjacent mutations;
- inspect route middleware/decorators/policies;
- inspect service-level ownership checks;
- inspect tenant scoping;
- inspect database-level policy when applicable.

Candidate omission:
A new or exceptional mutation bypasses an established authorization pattern.

## Grant/revoke lifecycle

If credentials/permissions can be granted:
- can they be revoked?
- do existing sessions/tokens retain access?
- does role removal propagate?

Domain evidence determines expected immediacy.

## Account deletion/disable

Possible implied consequences:
- session revocation;
- API key revocation;
- owned resource handling;
- scheduled job cancellation;
- external integration revocation.

Do not assume hard deletion is required.

## Tenant boundaries

If records belong to tenant/user:
- reads and writes should preserve ownership boundary;
- background jobs should carry tenant context where needed.

A missing filter is reportable only with clear reachability/evidence.

## UI is not enforcement

Never accept:
"button is hidden for non-admins"
as evidence of backend authorization.
