import sqlite3

conn = sqlite3.connect('jobs.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(Major_category, ShareWomen, Unemployment_rate)")

    Category = 'Engineering'
    Women = 0.5
    Unemployments = 0.1

    c.execute("INSERT INTO stuffToPlot VALUES(?, ?, ?)", (Category, Women, Unemployments))
    c.execute("select * from recent_grads where Major_category=:Category and ShareWomen>:Women and Unemployment_rate<:Unemployments", {"Category": Category, "Women": Women, "Unemployments": Unemployments})

    print(c.fetchall())

    conn.commit()
    c.close()
    conn.close()
    

create_table()