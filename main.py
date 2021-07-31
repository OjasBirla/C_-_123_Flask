from flask import Flask, jsonify, request

app = Flask(__name__)

data  = [{
    "ID": 1,
    "Name": "Ojas",
    "Contact": 9025316710,
    "Done": False
},
{
    "ID": 2,
    "Name": "Raju",
    "Contact": 5414515111,
    "Done": False
}]

@app.route("/add_data", methods=["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "Status": "Error" ,
            "Message": "Please provide the data"
       }, 400)
    
    Data  = [{
        "ID": data[-1]["ID"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "Done": False
    }]

    data.append(Data)

    return jsonify({
        "Status": "Succcess",
        "Message": "Added Successfuly"
    })


if __name__ == "__main__":
    app.run()
    