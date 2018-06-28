
// Module for mysql connection
var mysql = require('mysql');
// Module used for string formatting
var format = require('string-format');
format.extend(String.prototype, {});

var table_name = 'names';

function get_connection()
{
  // Function used for establishing Mysql connection
  var con = mysql.createConnection({
    host: "localhost",
    user: "popo",
    password: "popo",
    database: "popo"
  });
  con.connect(function(err){
    if(err)
    {
      console.log("Mysql connection error");
      throw err;
    }
  });
  return con;
}

exports.insert_data = function(first_name,last_name,response){
  // Function used for inserting user records into the table
  var con = get_connection();
  var sql = "INSERT INTO {0} VALUES('{1}','{2}')".format(table_name,
                                                         first_name,
                                                         last_name);
  con.query(sql, function (err, result) {
    if (err)
      throw err;
    response.send("Data inserted successfully");
  });
};

exports.select_data = function(first_name,res){
  // Function used for retrieving user records from the table
  var con = get_connection();
  var sql = "SELECT last_name FROM {0} WHERE first_name = '{1}' LIMIT 1"
            .format(table_name,first_name);
  con.query(sql,function(err,result){
    var last_name;
    if(result.length)
      last_name = result[0].last_name;
    else
      last_name = "Not Defined";
    res.render('display_data',{last_name:last_name});
  });
};
