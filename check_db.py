import sqlite3

conn = sqlite3.connect('storage/logs.db')
print(conn.execute('SELECT COUNT(*) FROM auth_logs').fetchone())
print(conn.execute('''
    SELECT event_type, COUNT(*) AS lignes, SUM(attempts) AS tentatives
    FROM auth_logs
    GROUP BY event_type
''').fetchall())
conn.close()