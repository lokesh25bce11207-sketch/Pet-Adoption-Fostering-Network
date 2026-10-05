USE pet_adoption_network;
-- Selection
SELECT name,species,age FROM animals WHERE current_status='Available' ORDER BY age DESC;
-- INNER JOINs
SELECT a.name,s.shelter_name FROM animals a JOIN shelters s ON a.shelter_id=s.shelter_id;
SELECT aa.application_id,ad.full_name,a.name,aa.application_status FROM adoption_applications aa JOIN adopters ad ON ad.adopter_id=aa.adopter_id JOIN animals a ON a.animal_id=aa.animal_id;
-- LEFT JOINs
SELECT s.shelter_name,a.name FROM shelters s LEFT JOIN animals a ON a.shelter_id=s.shelter_id;
SELECT ad.full_name,aa.application_id FROM adopters ad LEFT JOIN adoption_applications aa ON aa.adopter_id=ad.adopter_id;
SELECT a.name,m.next_checkup_date FROM animals a LEFT JOIN medical_records m ON m.animal_id=a.animal_id;
-- Aggregates / HAVING
SELECT species,COUNT(*) total FROM animals GROUP BY species;
SELECT shelter_id,COUNT(*) total FROM animals GROUP BY shelter_id HAVING COUNT(*)>=4;
SELECT f.foster_name,f.maximum_capacity,SUM(CASE WHEN fr.foster_status='Active' THEN 1 ELSE 0 END) occupied FROM foster_homes f LEFT JOIN fostering fr ON fr.foster_id=f.foster_id GROUP BY f.foster_id,f.foster_name,f.maximum_capacity;
-- Subqueries
SELECT name,age FROM animals WHERE age>(SELECT AVG(age) FROM animals);
SELECT name FROM animals WHERE animal_id IN(SELECT animal_id FROM adoption_applications WHERE application_status='Approved');
SELECT name,age FROM animals WHERE age>=ALL(SELECT age FROM animals WHERE species='Cat');
SELECT ad.full_name FROM adopters ad WHERE NOT EXISTS(SELECT 1 FROM adoption_applications aa WHERE aa.adopter_id=ad.adopter_id);
-- Set operator
SELECT name FROM animals WHERE species='Dog' UNION SELECT name FROM animals WHERE species='Cat';
-- Matching query
SELECT ad.full_name,a.name animal_name,s.shelter_name,a.health_status,a.special_needs,CONCAT('Species=',IF(ad.preferred_species IS NULL OR ad.preferred_species=a.species,'MATCH','NO'),' | Size=',IF(ad.preferred_size='Any' OR ad.preferred_size=a.size,'MATCH','NO')) reason FROM adopters ad JOIN animals a ON a.current_status='Available' AND (ad.preferred_species IS NULL OR ad.preferred_species=a.species) AND (ad.preferred_size='Any' OR ad.preferred_size=a.size) LEFT JOIN shelters s ON s.shelter_id=a.shelter_id;
-- Views
SELECT * FROM Available_Animals_View; SELECT * FROM Medical_Followup_View WHERE followup_state IN('OVERDUE','UPCOMING'); SELECT * FROM Adoption_Application_Summary_View;
-- TCL / SAVEPOINT demonstration
START TRANSACTION; UPDATE animals SET health_status='Temporary Test' WHERE animal_id=1; SAVEPOINT s1; UPDATE animals SET health_status='Another Test' WHERE animal_id=2; ROLLBACK TO SAVEPOINT s1; ROLLBACK;
