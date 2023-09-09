from data_base import db
from headers import session
from user_id import user_id

class Friends():
    # создать таблицу
    def base_friends():       
        cur = db.cursor()  
        cur.execute('''CREATE TABLE FRIENDS  
            (id INT NOT NULL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL);''')

        print("Table created successfully")
        db.commit()  


    # получить имена друзей
    def get_friends(friends_list):
        friends = session.method('friends.get', {
            'user_id': user_id,  
            'order': 'name',
            'list_id': None,
            'count': None,
            'offset': None,
            'fields': 'nickname',
            'name_case': None,
            'ref': 255
        })
        
        
        a = int(friends['count'])
        for i in range(0,a):
            id = friends['items'][i]['id']
            friends_list[id] = {}
            friends_list[id]['first_name'] = friends['items'][i]['first_name']
            friends_list[id]['last_name'] = friends['items'][i]['last_name']
        
        Friends.insert_db(friends_list)
        

    # записать друзей в таблицу        
    def insert_db(friends_list):
        cur = db.cursor()
        for i in friends_list:
            id = i
            first_name = friends_list[i]['first_name']
            last_name = friends_list[i]['last_name']
            
            cur.execute(
                "INSERT INTO FRIENDS (id,first_name,last_name) VALUES (%s,%s,%s);", (id,first_name,last_name)
                
            )

        db.commit()  
        print("Record inserted successfully")  
