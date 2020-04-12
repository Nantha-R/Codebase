/*
The DATE_TRUNC function truncates a time stamp expression or literal based on the date part that you specify,
such as hour, week, or month. DATE_TRUNC returns the first day of the specified year, the first day of the specified
month, or the Monday of the specified week.
*/

/* Resources : https://docs.aws.amazon.com/redshift/latest/dg/r_DATE_TRUNC.html */

/* Eg SQL QUERY for week */

select date_trunc('week', employee_joining_time) as Employee_joining_time
from Occupations group by Employee_joining_time;

/* Output */

Employee_joining_time |
----------------------|
2008-09-01            |
2008-09-08            |
2008-09-15            |

/* Eg SQL QUERY for day */

select date_trunc('day', employee_joining_time) as Employee_joining_time
from Occupations group by Employee_joining_time;

/* Output */

Employee_joining_time |
----------------------|
2008-09-01            |
2008-09-02            |
2008-09-03            |
