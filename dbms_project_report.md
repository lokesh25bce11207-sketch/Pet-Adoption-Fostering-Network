# Pet Adoption & Fostering Network — CSE3001
## Abstract
A normalized relational DBMS and Flask application for shelters, animals, adopters, foster homes, medical records, applications, visits and adoptions.
## Objectives
Demonstrate ER modeling, relational schema design, normalization, SQL, PL/SQL concepts, indexes, triggers, procedures, query optimization, transactions, concurrency and recovery.
## Design
SHELTERS 1:N ANIMALS; ANIMALS 1:N MEDICAL_RECORDS; ADOPTERS 1:N APPLICATIONS; APPLICATIONS 1:N HOME_VISITS; ANIMALS/FOSTER_HOMES M:N through FOSTERING; approved APPLICATIONS create ADOPTION_RECORDS.
## Normalization
1NF: atomic values. 2NF: no partial dependencies. 3NF: no transitive dependencies. BCNF: every determinant is a candidate key. 4NF example: independently multi-valued adopter preferences should be split into separate relations.
## SQL
DDL, DML, TCL, joins, nested queries, aggregate functions, set operations, views, indexes and constraints are implemented.
## Triggers
Medical overdue alert on row insertion; adoption status synchronization; foster capacity validation. A normal trigger cannot detect passage of time without a row event, so Generate_Overdue_Medical_Alerts is provided.
## Procedures
Approve_Adoption atomically validates approved application + completed recommended home visit + non-adopted animal. Other procedures generate medical alerts and availability reports.
## Storage/Indexing/Optimization
B+ trees support ordered index access; hashing supports equality lookup. Query cost considers I/O, CPU, memory and intermediate results. Heuristics push filters early; cost-based optimizers compare plans. Use EXPLAIN for the actual MySQL plan.
## Transactions/Recovery
Adoption is a transaction. COMMIT persists, ROLLBACK undoes uncommitted changes, SAVEPOINT permits partial rollback. Serializability, locks, deadlock, timestamp ordering, 2PC and undo/redo recovery are covered conceptually in academic_topics.md.
## Limitations
Academic project; no production authentication/payment/identity verification.
## Future scope
Role-based access, notifications, mobile UI, analytics and cloud deployment.
