import sqlite3

def get_all(query):
    try:
        conn = sqlite3.connect("data/databaseapi")
        data = conn.execute(query).fetchall()
        return data
    except sqlite3.Error as e:
        print("Lỗi kết nối hoặc thực thi truy vấn:", str(e))
        return None
    finally:
        if conn:
            conn.close()

def get_news_by_id(news_id):
    conn = sqlite3.connect("data/databaseapi")
    data = conn.execute(news_id).fetchall()
    sql = ''' 
    SELECT N.subject, N.description ,N.image , N.original_url, C.name, 
     C.url FROM news N INNER JOIN catalogy C ON N.catalogy_id=C.id 
     WHERE id=?
    '''
    return data
    conn.close()
if __name__ == "__main__":
    result = get_all("SELECT * FROM catalogy")
    if result:
        for row in result:
            print(row)
