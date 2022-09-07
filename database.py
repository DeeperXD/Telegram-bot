import sqlite3


# контакт дс, про себе, підписка на новини та івенти, стать
def add_user(user):
    sql_command(f"INSERT INTO users VALUES ({user.telegram_id})")


def remove_user(telegram_id):
    sql_command(f"DELETE FROM users WHERE telegram_id = {telegram_id}")


def check_user_exist(user_id):
    res = sql_command_r(f'SELECT * FROM users WHERE telegram_id == {user_id}')
    return len(res) > 0


def sql_command(command):
    conn = sqlite3.connect('users.dt')
    c = conn.cursor()
    c.execute(command)

    conn.commit()
    conn.close()


def sql_command_r(command):
    conn = sqlite3.connect('users.dt')
    c = conn.cursor()
    c.execute(command)
    res = c.fetchall()
    conn.commit()
    conn.close()

    return res


async def sql_command_promp():
    command = input("enter sql command")
    conn = sqlite3.connect('users.dt')
    c = conn.cursor()
    try:
        c.execute(command)
    except:
        print(f"error to execute command")

    conn.commit()
    conn.close()


async def sql_print():  # SELECT * FROM users
    command = input("enter sql command: ")
    conn = sqlite3.connect('users.dt')
    c = conn.cursor()
    try:
        c.execute(command)
        print(c.fetchall())
    except:
        print(f"error to execute command")


    conn.commit()
    conn.close()


