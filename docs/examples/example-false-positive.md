# Example Finding Format — Suppressed False Positive

> [!NOTE]
> This document is a non-executable documentation example illustrating how Missing Piece formats hypothetical audit findings. It is purely illustrative and does not reflect any software defect in this package.

## Initial candidate

`User` can be deleted. `ProfileImage` objects exist in object storage. No explicit `deleteProfileImage()` call appears in the application service.

Initial hypothesis:
> User deletion leaks profile images.

## Counter-evidence

Repository infrastructure config contains an object-storage lifecycle rule that deletes objects under `users/<id>/` after the owning user deletion marker is written.

The deletion service writes that marker.

## Result

**No finding.**

Reason:
Cleanup is externally owned by the storage lifecycle mechanism and is reachable from the deletion flow.

This example demonstrates why Missing Piece must not equate "not visible in the service function" with "missing."
