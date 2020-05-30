/*
DATEDIFF returns the difference between the date parts of two date or time expressions.
*/

/* Resources : https://docs.aws.amazon.com/redshift/latest/dg/r_DATEDIFF_function.html */

/* Eg SQL QUERY */

/* Calculating difference in unit of week */
select datediff(WEEK,'2009-01-01','2009-12-31') as numweeks;

/* Calculating difference in unit of day */
select datediff(DAY,'2009-01-01','2009-12-31') as numweeks;

/* Calculating difference in unit of second */
select datediff(SECOND,'2009-01-01','2009-12-31') as numweeks;

