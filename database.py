import psycopg2

global USERID


# MENU FUNCTIONS
def create_user(name, email, password):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    if email.find('@') != -1:
        if email.find('@netflox.com') == -1:
            c.execute("INSERT INTO users (nome, email, password, balance) VALUES ('" + name + "','" + email + "','" + password + "',20)")
        else:
            print("\n\tCan't create accounts under netflox domain")
    else:
        print("\n\tInsert a valid email address")

    conn.commit()
    conn.close()


def log_in(email, password):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    if email.find('@netflox.com') == -1:
        c.execute("SELECT * FROM users WHERE email = '" + email + "' AND password = '" + password + "'")
        results = c.fetchall()

        global USERID

        conn.commit()
        conn.close()

        if results:
            print("\n\tWelcome " + results[0][1] + ", your balance is " + str(results[0][4]))
            USERID = results[0][0]
            return 1  # client
        else:
            print("\n\tEmail and password not recognised")
            return 0

    elif email.find('@netflox.com') != -1:
        c.execute("SELECT * FROM users WHERE email = '" + email + "' AND password = '" + password + "'")
        results = c.fetchall()

        conn.commit()
        conn.close()

        if results:
            for i in results:
                print("\n\tWelcome Admin " + i[1])
                USERID = i[0]
                return -1  # admin
        else:
            print("\n\tEmail and password not recognised\n")
            return 0


# MESSAGES CLIENT
def show_unread_messages(userid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    c.execute("SELECT * FROM messages WHERE users_userid = " + str(userid) + " AND bolread = FALSE")
    messages = c.fetchall()

    y = 0
    print("\r")
    for i in messages:
        c.execute("SELECT * FROM users WHERE userid = " + str(i[4]))
        sender = c.fetchall()
        for x in sender:
            y += 1
            print("\t" + str(y) + ") Message from " + x[1] + " date: " + str(i[5]))

    print("\t0) Exit")

    conn.commit()
    conn.close()

    return messages


def show_read_messages(userid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    c.execute("SELECT * FROM messages WHERE users_userid = " + str(userid) + " AND bolread = TRUE")
    messages = c.fetchall()

    y = 0
    print("\n")
    for i in messages:
        c.execute("SELECT * FROM users WHERE userid = " + str(i[4]))
        sender = c.fetchall()
        for x in sender:
            y += 1
            print("\t" + str(y) + ") Message from " + x[1] + " date: " + str(i[5]))

    print("\t0) Exit")

    conn.commit()
    conn.close()

    return messages


def read_message(msgid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    c.execute("UPDATE messages SET bolread = TRUE WHERE msgid='" + str(msgid) + "'")

    conn.commit()
    conn.close()


# ADMIN
def add_article(name, actorid, director, imbdrating, genre, price, year, monthsavaible, type):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    # TODO multiple actor id
    c.execute(
        "INSERT INTO movies(name, actorid, director, year, imdbrating, genre, price, timeavaible, type) VALUES('" + name + "','" + actorid + "','" + director + "', '" + year + "','" + imbdrating + "','" + genre + "','" + price + "','" + monthsavaible + "','" + type + "')")
    print("\n\t" + name + " was added to movies")

    conn.commit()
    conn.close()


def change_price(n_id, newprice):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    itemid = n_id
    if isinstance(n_id, str):
        c.execute("SELECT itemid FROM movies WHERE name = '" + n_id + "'")
        n_id = c.fetchall()
        for i in n_id:
            itemid = i[0]

    c.execute("SELECT price FROM movies WHERE itemid = '" + str(itemid) + "'")
    result = c.fetchall()
    oldprice = 0
    for i in result:
        oldprice = i[0]

    c.execute("UPDATE movies SET price = '" + str(newprice) + "' WHERE itemid = '" + str(itemid) + "'")
    c.execute(
        "INSERT INTO pricehistory(oldprice, data, movies_itemid) VALUES('" + str(oldprice) + "', CURRENT_DATE,'" + str(
            itemid) + "')")

    print("\n\tPrice updated successfully")
    print("\tOld price saved to history")

    conn.commit()
    conn.close()


def remove_article(n_id):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    itemid = n_id
    if isinstance(n_id, str):
        c.execute("SELECT itemid FROM movies WHERE name = '" + n_id + "'")
        n_id = c.fetchall()
        for i in n_id:
            itemid = i[0]

    c.execute("SELECT * FROM rent WHERE movieid = '" + str(itemid) + "' AND timeavaible > 0")
    result = c.fetchall()
    if result:
        print("\n\tCan't remove article because there are user(s) renting it")
    else:
        c.execute("DELETE FROM movies WHERE itemid = '" + str(itemid) + "'")
        print("\n\tArticle removed successfully")

    conn.commit()
    conn.close()


def message_all(msg, senderid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    c.execute("SELECT userid FROM users")
    results = c.fetchall()

    c.execute("SELECT Sum(pg_column_size(userid))/4 as total_size FROM users")
    size = c.fetchall()[0][0]

    i = 0
    while i < size:
        if results[i][0] != senderid:
            c.execute(
                "INSERT INTO messages (message, bolread, users_userid, senderid, data) VALUES ('" + msg + "', FALSE, '" + str(
                    results[i][0]) + "', '" + str(senderid) + "', CURRENT_DATE)")
        i += 1

    print("\n\tMessage sent to all")

    conn.commit()
    conn.close()


def message_client(msg, recieverid, senderid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    c.execute(
        "INSERT INTO messages (message, bolread, users_userid, senderid, data) VALUES ('" + msg + "', FALSE, '" +
        str(recieverid) + "', '" + str(senderid) + "', CURRENT_DATE)")

    print("\n\tMessage sent successfully")

    conn.commit()
    conn.close()


def alter_balance(userid, balance):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()

    c.execute("UPDATE users SET balance = '" + str(balance) + "' WHERE userid='" + str(userid) + "'")

    print("\n\tBalance updated successfully")

    conn.commit()
    conn.close()


def view_allmovies():  # imprime os filmes
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    movies = c.fetchall()
    print('\n')
    for x in movies:
        print('\t'+x[1])
    print('\n')
    conn.commit()
    conn.close()


def view_movieinfo(movie):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE name = '" + movie + "'")
    movies = c.fetchall()
    x = 0
    for x in movies:
        print(x)

    if movies:
        pass
    else:
        print("\n\tMovie name not correct")
        return 0

    conn.commit()
    conn.close()

    return x[1]


def view_saldo(userid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE userid = '" + str(userid) + "'")
    results = c.fetchall()
    x = 0
    for x in results:
        print(x[4])
    conn.commit()
    conn.close()
    return x[4]


def view_custo(movie):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE name = '" + movie + "'")
    results = c.fetchall()
    x = 0
    for x in results:
        print(x[6])
    conn.commit()
    conn.close()
    return x[6]


def compra_filme(custo, saldo, USERID):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    saldofinal = saldo - custo
    c.execute("UPDATE users  SET balance=(%s) WHERE userid='" + str(USERID) + "'", (saldofinal,))
    conn.commit()
    conn.close()


def create_rent(custo, userid, moviename):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE name ='" + moviename + "'")
    results = c.fetchall()
    x = 0
    for x in results:
        break

    c.execute("SELECT * FROM users WHERE userid ='" + str(userid) + "'")
    results2 = c.fetchall()
    y = 0
    for y in results2:
        break

    type = x[9]
    c.execute(
        "INSERT INTO rent(clientid,date,price,dateend,usermail,timeavaible,type,movieid) VALUES ( %s, CURRENT_TIMESTAMP , %s, CURRENT_TIMESTAMP + %s * INTERVAL '1 month',%s,%s,'" + type + "',%s)",
        (y[0], custo, x[8], y[2], x[8], x[0]))  # falta  tempo aos filmes

    c.execute("SELECT date + timeavaible * INTERVAL '1 month' FROM rent;")
    results3 = c.fetchall()
    for z in results3:
        break

    # c.execute("INSERT INTO rent(dateend) VALUES('z')")

    conn.commit()
    conn.close()


def view_rent(userid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM rent WHERE clientid = '" + str(userid) + "'")
    results = c.fetchall()
    for x in results:
        print(x)

    conn.commit()
    conn.close()


def view_available_movies(userid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM rent WHERE dateend >= CURRENT_TIMESTAMP AND clientid='" + str(userid) + "'")
    results = c.fetchall()
    print("\n\t------------")
    print("\tMovies available:")
    for x in results:
        c.execute("SELECT * FROM movies WHERE itemid =  " + str(x[8]))
        movies = c.fetchall()
        for y in movies:
            print("\t"+y[1])

    print("\t------------")
    print("\tMovies not available any more:")
    c.execute("SELECT * FROM rent WHERE CURRENT_TIMESTAMP > dateend  AND clientid='" + str(userid) + "'")
    results2 = c.fetchall()

    for z in results2:
        z[8]
        c.execute("SELECT * FROM movies WHERE itemid =  " + str(z[8]))
        movies2 = c.fetchall()
        for r in movies2:
            print("\t"+r[1])
    print("\t------------")


def findby_name(name):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE name like '%" + name + "%'")
    movies = c.fetchall()
    for x in movies:
        print(x)

    if movies:
        for i in movies:
            break
    else:
        print("\n\t---movie name not correct---")
        return 0
    print("\n")
    conn.commit()
    conn.close()


def findby_director(director):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE director like '%" + director + "%'")
    movies = c.fetchall()
    for x in movies:
        print("\t"+x[3] + "----" + x[1])

    if movies:
        for i in movies:
            break
    else:
        print("\t\n---movie director name not correct---")
        return 0
    print("\n")
    conn.commit()
    conn.close()


def findby_type(type):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE type like '%" + type + "%'")
    movies = c.fetchall()
    for x in movies:
        print("\t"+x[9] + "----" + x[1])

    if movies:
        for i in movies:
            break
    else:
        print("\n\t---movie type not correct---")
        conn.commit()
        conn.close()
        return 0
    print("\n")
    conn.commit()
    conn.close()


def findby_actor(actor):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM actors WHERE name like('%" + actor + "%')")
    # c.execute("SELECT * FROM actors WHERE movieid['"+str(n)+"']=5")
    actors = c.fetchall()
    x = 0
    for x in actors:
        break
    id = x[2]
    size = len(id)
    for y in range(0, size):
        c.execute("SELECT * FROM movies WHERE itemid=('" + str(id[y]) + "')")
        movies = c.fetchall()
        for z in movies:
            print("\t"+x[1], "----", z[1])
    conn.commit()
    conn.close()


def view_allmovies_ordertitle():
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies ORDER BY name;")
    movies = c.fetchall()
    for x in movies:
        print("\t"+x[1])
    conn.commit()
    conn.close()


def view_allmovies_orderdirector():
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies ORDER BY director;")
    movies = c.fetchall()
    for x in movies:
        print("\t"+x[3] + "---" + x[1])
    conn.commit()
    conn.close()


def view_allmovies_orderdate():
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies ORDER BY year;")
    movies = c.fetchall()
    for x in movies:
        print("\t"+str(x[7]) + "------" + x[1])
    conn.commit()
    conn.close()


def view_allmovies_orderimdb():
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM movies ORDER BY imdbrating;")
    movies = c.fetchall()
    for x in movies:
        print("\t"+str(x[4]) + "-----" + x[1])
    conn.commit()
    conn.close()


# def view_availablemovies_ordertitle(USERID):


def view_availablemovies_orderdirector(userid):
    conn = psycopg2.connect("host=localhost dbname=projeto user=postgres password=postgres")
    c = conn.cursor()
    c.execute("SELECT * FROM rent WHERE dateend >= CURRENT_TIMESTAMP AND clientid='" + str(userid) + "'")
    results = c.fetchall()
    print("\t------------")
    print("\tMovies available:")
    movies = 0
    for x in results:
        id = x[8]  # id's que queremos ir buscar
        print(id)
        c.execute("SELECT * FROM movies WHERE itemid = '" + str(id) + "' ORDER BY director")
        movies += c.fetchall()
    for y in movies:
        print("\t"+y[3] + "---" + y[1])

    print("\t------------")
    print("\tMovies not available any more:")
    c.execute("SELECT * FROM rent WHERE CURRENT_TIMESTAMP > dateend  AND clientid='" + str(userid) + "'")
    results2 = c.fetchall()
    id = 0
    for z in results2:
        id2 = z[8]
        c.execute("SELECT * FROM movies WHERE itemid = " + str(z[8]))
        movies2 = c.fetchall()
        for r in movies2:
            print("\t"+r[1])
    print("\t------------")

# def view_availablemovies_orderdate(USERID):
# def view_availablemovies_orderimdb(USERID):
