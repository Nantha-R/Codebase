/* The ROUND() function rounds a number to a specified number of decimal places. */

/* Resources : https://www.w3schools.com/sql/func_sqlserver_round.asp */

/* Eg SQL QUERY for calculating percentage between two numbers with one decimal places */

Select ROUND(3/100 * 100, 1) as percentage;

/* Output */

percentage |
3.0

/* Eg SQL QUERY for calculating percentage between two numbers with two decimal places */

Select ROUND(3/100 * 100, 2) as percentage;

/* Output */

percentage |
3.00


