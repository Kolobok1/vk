from user_id import user_id
from headers import session
from data_base import db

class Online_friends():
    
    # получить список друзей в сети
    def check_online_friends(wel):

        friends = session.method('friends.getOnline',{
            'user_id': user_id,
            'list_id': None,
            'online_mobile': None,
            'order': None,
            'count': None,
            'offset': None
        })

        print (friends)
        wel = Online_friends.db_add(wel,friends)
        return wel
        
    # работа со столбцами
    def db_add(wel,friends):
        wel += 1
        name = 'online' + str(wel)
        
        # добавить столбец в таблицу
        cur = db.cursor()
        cur.execute(
            f'''
            ALTER TABLE FRIENDS ADD COLUMN {name} integer;
            
            ''', name
        )
        
        # отметить тех кто в сети
        sql = f"UPDATE friends SET {name} = CASE"
        for friend in friends:
            sql = sql + f" WHEN id = {friend} THEN 1 "
        sql = sql + ' END;'
        db.commit()
        
        cur.execute(sql)
        db.commit()
        
        return wel