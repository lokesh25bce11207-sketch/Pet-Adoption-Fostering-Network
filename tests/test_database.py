import os,mysql.connector
def test_connection():
 c=mysql.connector.connect(host=os.getenv('DB_HOST','127.0.0.1'),port=int(os.getenv('DB_PORT','3306')),user=os.getenv('DB_USER','root'),password=os.getenv('DB_PASSWORD',''),database=os.getenv('DB_NAME','pet_adoption_network')); cur=c.cursor(); cur.execute('SELECT 1'); assert cur.fetchone()[0]==1; cur.close(); c.close()
