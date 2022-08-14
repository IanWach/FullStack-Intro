import psycopg2

conn = psycopg2.connect(" user='postgres' password="'ianno2'" dbname=example")
cursor = conn.cursor()

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS todo;")

cur.execute("""
CREATE TABLE todo(
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL);
    """)
cur.execute("""
INSERT INTO todo (id, description) VALUES (1, 'This it');
""")

cur.execute("""
INSERT INTO todo (id, description) VALUES (2, 'This not');
""")
cur.execute("""
INSERT INTO todo (id, description) VALUES (3, 'This it is');
""")
    
conn.commit()
cur.close()
conn.close()