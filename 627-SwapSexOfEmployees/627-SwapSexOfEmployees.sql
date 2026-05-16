-- Last updated: 5/16/2026, 12:27:20 PM
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;

