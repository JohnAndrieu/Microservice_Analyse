# src/app/main.py

from flask import Flask, jsonify
import happybase
import string
app = Flask(__name__)

outputDir = "../app/out"

@app.route("/results_analyses/csv")
def hbaseCSV():
    c = happybase.Connection(host='192.168.37.40',port=50001)

    # Get the full list of tables
    tables = c.tables()

    # For each table in the tables
    for table in tables:
        # Open file to write to
        file = open(outputDir + "/" + str(table, 'utf-8') + ".csv", "w+")

        t = c.table(table)

        print(str(table, 'utf-8') + ": ")
        count = 0

        try:
            data = t.scan()

            for col in data:
                #print(col)
                row = str(col[0], 'utf-8')
                values = ""
                file.write(f'{row}')
                for column, value in col[1].items():
                    column = str(column, 'utf-8')
                    value = str(value, 'utf-8')
                    file.write(f'\t{value}')
                #print(values)
                #Write row, column, value to file
                file.write(f'\n')
                count += 1
        except:
            return "Error check logs"

    return jsonify({"message":"Done"})

@app.route("/data")
def index():
    connection = happybase.Connection(host='192.168.37.40',port=50001)
    table = connection.table('test1')
    data = table.scan()
    for col in data:
        print("col : ",col)
    
    return jsonify({"message":str(table.rows('1:2'))})
        
if __name__ == '__main__':
    app.run(host='192.168.1.156', port=50003, debug=True)