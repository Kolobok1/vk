import asyncio,time

from friends import Friends
from online_user import Get_online
from data_base import db

# проверить онлайн пользователя    
async def check_online(wel):
    num = False
    while True:
        num,wel =  Get_online.check_online(num,wel)
        asyncio.sleep(5)    

        if num == False:
            time.sleep(3)

# получить название последнего столбца и записать счетчик
def get_wel():
    try:
        cur = db.cursor()
        cur.execute("select * from friends")
        wel = [desc[0] for desc in cur.description][-1][6:]
        
        wel = int(wel)
    except:
        wel = 0
    return wel

async def main():

    wel = get_wel()
            
    
    task1 = asyncio.create_task(check_online(wel))
    await task1

    db.close()

# проверить есть ли таблица
def check_table():
    friends_list = {}
    cur = db.cursor()
    cur.execute(
        '''SELECT EXISTS (
        SELECT 1
        FROM   information_schema.tables 
        WHERE  table_name = 'friends'
        );
        '''
    )
    tabl = cur.fetchone()[0]
    
    if tabl == False:
        print('Adding a table')
        
        # получить список друзей 
        Friends.base_friends()
        Friends.get_friends(friends_list)
    
    asyncio.run(main())


if __name__ == '__main__':
    check_table()
    