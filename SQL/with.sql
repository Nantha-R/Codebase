/*
The SQL WITH clause allows you to give a sub-query block a name (a process also called sub-query refactoring),
which can be referenced in several places within the main SQL query.
*/

/* Resources : https://www.geeksforgeeks.org/sql-with-clause/ */

/* Eg SQL QUERY with one Sub-query: */

WITH EMPLOYEE_NAMES (
SELECT employee_name from Occupations
)

SELECT employee_name from EMPLOYEE_NAMES;

/* Eg SQL QUERY with multiple sub queries: */

WITH EMPLOYEE_SALARY (
SELECT SUM(salary) AS sum_of_salary from Occupations
), EMPLOYEE_TAX AS (
SELECT SUM(tax) AS sum_of_tax from Occupations
)

SELECT sum_of_salary, sum_of_tax from EMPLOYEE_SALARY, EMPLOYEE_TAX;
