from flask import Flask, render_template, make_response, request
from pydantic import BaseModel
from flask_pydantic import validate
import pandas as pd
import numpy as np
import json
import sqlite3




app = Flask(__name__)

conn = sqlite3.connect('my_data.db', check_same_thread=False)
conn.row_factory = sqlite3.Row


@app.route('/first5')
def index():
    conn = sqlite3.connect('my_data.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    rows = conn.execute('SELECT * FROM top250 LIMIT 5').fetchall()
    print(rows)
    conn.close()
    return render_template('print_items.html', rows=rows)



								
@app.route('/add_player',methods = ['POST', 'GET'])
def addrec():
    con = sqlite3.connect("my_data.db")
    if request.method == 'POST':
        try:
         Name = request.json['Name']
         Position = request.json['Position']
         Age = request.json['Age']
         Team_from = request.json['Team_from']
         League_from = request.json['League_from']
         Team_to = request.json['Team_to']
         League_to = request.json['League_to']
         Season = request.json['Season']
         Market_value = request.json['Market_value']
         Transfer_fee = request.json['Transfer_fee']

         
         cur = con.cursor()
            
         cur.execute("INSERT INTO top250 (Name,Position,Age,Team_from,League_from,Team_to,League_to,Season,Market_value,Transfer_fee) VALUES (?,?,?,?,?,?,?,?,?,?)",(Name,Position,Age,Team_from,League_from,Team_to,League_to,Season,Market_value,Transfer_fee) )
            
         con.commit()
         msg = "Record successfully added"
        except:
         con.rollback()
         msg = "error in insert operation"
    
        finally:
            con.close()
            return render_template("result.html",msg = msg)
            


@app.route('/list')
def list():
   con = sqlite3.connect("my_data.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from top250")
   
   rows = cur.fetchall();
   return render_template('print_items.html', rows=rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)