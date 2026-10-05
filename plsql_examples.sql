-- CSE3001 PL/SQL companion for an Oracle lab. Main application uses MySQL 8.
DECLARE v_name animals.name%TYPE; BEGIN SELECT name INTO v_name FROM animals WHERE animal_id=1; DBMS_OUTPUT.PUT_LINE(v_name); EXCEPTION WHEN NO_DATA_FOUND THEN DBMS_OUTPUT.PUT_LINE('Animal not found'); END; /
DECLARE CURSOR c IS SELECT name,species FROM animals; BEGIN FOR r IN c LOOP DBMS_OUTPUT.PUT_LINE(r.name||' - '||r.species); END LOOP; END; /
CREATE OR REPLACE PROCEDURE get_animal(p_id IN NUMBER) AS v_name VARCHAR2(80); BEGIN SELECT name INTO v_name FROM animals WHERE animal_id=p_id; DBMS_OUTPUT.PUT_LINE(v_name); EXCEPTION WHEN NO_DATA_FOUND THEN DBMS_OUTPUT.PUT_LINE('Animal not found'); END; /
CREATE OR REPLACE FUNCTION get_animal_status(p_id IN NUMBER) RETURN VARCHAR2 IS v_status VARCHAR2(30); BEGIN SELECT current_status INTO v_status FROM animals WHERE animal_id=p_id; RETURN v_status; END; /
