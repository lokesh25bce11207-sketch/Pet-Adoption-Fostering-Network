# Relational Algebra / Tuple Relational Calculus
The syllabus requires selection, projection, joins, division, set operations, renaming and tuple relational calculus.

Selection: σ current_status='Available' (ANIMALS)
Projection: π name,species (ANIMALS)
Rename: ρ A(ANIMALS)
Join: ANIMALS ⋈ ANIMALS.shelter_id=SHELTERS.shelter_id SHELTERS
Division: find adopters related to every required home-readiness condition; this represents a “for all” query.
Set operations: Dogs UNION Cats; all animals DIFFERENCE adopted animals.
Tuple relational calculus example: {a.name | ANIMALS(a) AND a.current_status='Available'}
SQL equivalents are in queries.sql.
