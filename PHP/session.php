<?php
  // Starts a session
  session_start();

  // Check if a session is started or not
  if (session_status() == PHP_SESSION_NONE) {
    // Evaluates to True if a session has started
  }
  // REF: https://stackoverflow.com/questions/6249707/check-if-php-session-has-already-started

  // Set a session variable
  $_SESSION['key'] = 'value';

  // Unset or remove a session variable
  unset($_SESSION['key'])
  // Can unset a variable without even checking if
  // the variable is set or not.
  // REF : https://stackoverflow.com/questions/1374705/check-if-var-exist-before-unsetting-in-php

  // Get a session variable
  value = $_SESSION['key']

  // Unset all variables
  session_unset();

  // Destroy a session
  session_destroy();
  // REF : https://stackoverflow.com/questions/4303311/what-is-the-difference-between-session-unset-and-session-destroy-in-php
?>
