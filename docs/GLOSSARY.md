# Glossary

**Absence analysis**  
Reasoning about behavior that should exist but cannot be established.

**Observed fact**  
Repository-grounded evidence about what the system does.

**Implication rule**  
A general relationship that turns an observed fact into an expected counterpart.

**Expected counterpart**  
Behavior, guard, transition, cleanup, recovery, or other element logically implied by the observed system.

**Candidate omission**  
An expected counterpart not found during initial search.

**Counter-evidence**  
Evidence that disproves or weakens a candidate omission.

**Finding**  
A candidate omission that survives verification and meets reporting threshold.

**Symmetry**  
A relationship between operations that often have inverses or counterparts.

**Lifecycle completeness**  
Whether a resource can move intentionally from creation through termination/cleanup.

**Reachability**  
Whether present code actually participates in the relevant runtime path.

**Confidence**  
Certainty that the omission claim is correct.

**Severity**  
Potential impact if the omission is real.

**Root omission**  
The underlying missing behavior that may create multiple symptoms.

**Coverage**  
Areas of the system and detector families meaningfully inspected.
