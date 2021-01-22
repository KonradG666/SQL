import sqlite3

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def add_projekt(conn, projekt):
   """
   Create a new projekt into the projects table
   :param conn:
   :param projekt:
   :return: projekt id
   """
   sql = '''INSERT INTO projects (nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, projekt)
   conn.commit()
   return cur.lastrowid

def add_task(conn, task):
    """
     Create a new task into the tasks table
     :param conn:
     :param task:
     :return: task id
     """
    sql = '''INSERT INTO task (projekt_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sgl, task)
    conn.commit()
    return cur.lastrowid

def select_task_by_status(conn, status):
   """
   Query tasks by priority
   :param conn: the Connection object
   :param status:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM tasks WHERE status=?", (status,))

   rows = cur.fetchall()
   return rows

if __name__ == "__main__":
    conn = create_connection("database1.db")
    projekt = [("Powtórka z funkcji", "2020-05-11 00:00:00", "2020-05-13 00:00:00"),
               ("Pompki", "2021-01-15 00:00:00", "2021-01-17 00:00:00")]
    pr_id = add_projekt(conn, projekt)



    task = [(
        pr_id,
        "Funkcje w obiektach",
        "top titles",
        "started",
        "2020-05-11 00:00:00",
        "2020-05-13 00:00:00"
    ),
    (   pr_id,
        "Funkcje w obiektach",
        "generate_views",
        "started",
        "2020-05-11 00:00:00",
        "2020-05-13 00:00:00"
    ),
    (   pr_id,
        "100 pompek",
        "4 x 25",
        "started",
        "2020-05-11 00:00:00",
        "2020-05-13 00:00:00"
     )
    ]

    task_id = add_task(conn, task)
    print(pr_id, task_id)
    conn.commit()


