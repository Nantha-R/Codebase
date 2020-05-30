/*
The SQL PERCENTILE_CONT is one of the Analytic Function, which will calculate a percentile based on the
continuous distribution of column values in a table.
*/

/* Resources : https://www.tutorialgateway.org/sql-percentile_cont/ */

/* Eg SQL QUERY */

Select
percentile_cont(0.50) within group (order by salary) as salary_p50,
percentile_cont(0.99) within group (order by salary) as salary_p99,
percentile_cont(0.9999) within group (order by OUR_PRICE) as salary_p99_99
from Occupations;
