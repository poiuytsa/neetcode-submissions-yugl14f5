-- Write your query below
SELECT employee_id, CASE 
    WHEN employee_id%2=1 AND name NOT LIKE 'M%' THEN salary
    else 0 
    END AS bonus
FROM employees 
ORDER BY employee_id
