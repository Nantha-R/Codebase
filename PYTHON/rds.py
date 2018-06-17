class rds:

    def get_connection(self,rds_host_name, db_user_name,db_password,db_name,connect_timeout):
        """Initiate DB Connection"""
        try:
            conn = pymysql.connect(rds_host_name,
                                   user=db_user_name,
                                   passwd=db_password,
                                   db=db_name,
                                   connect_timeout=connect_time_out)
            return conn
        except:
            raise Exception("Connection to database failed")

    def get_results(self,db_conn,table_name):
        """Retrieving records from the database"""
        try:
            with db_conn.cursor() as cur:
                query = ("SELECT * FROM {}".format(table_name))
                cur.execute(query)
                return cur.fetchall()
        except Exception as e:
            raise Exception("Retrieving records from the database "
                            "failed with an exception : %s" % str(e))

    def __insert_into_db(self, db_conn, table_name,insert_value):
        """Insert records into DB"""
            with db_conn.cursor() as cur:
                try:
                    query = ('INSERT INTO {} VALUES(%s,%s)'
                             .format(table_name))
                    cur.executemany(query, insert_value)
                    db_conn.commit()
                except Exception as e:
                    raise Exception(e)
