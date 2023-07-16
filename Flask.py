from flask import Flask, jsonify, request 

app = Flask(__name__)

data= [
        {
            'id': 1,
            'Name': 'Raju',
            'Contact': "9988776655",
            'done': False,
        },
        {
            'id': 2,
            'Name': 'Rahul',
            'Contact': "1111111112",
            'done': False,
        }
    ]


@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data! "
        },400)
    contact = {
        'id': tasks[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
        }

    data.append(contact)
    return jsonify({
        "status": "success",
        "message": "Data added successfully! "
     })

@app.route("/get-data")
def get_data():
    return jsonify({
        'data': data
    })


if __name__ == "__main__":
    app.run(debug= True)