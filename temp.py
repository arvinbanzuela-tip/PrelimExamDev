from flask import Flask, jsonify, request

app = Flask (__name__)
temp = [

    {
        "temp_id" : "1",
        "date" : "1/10/2022",
        "temperature" : "34° celcius"
    },
    {
        "temp_id" : "2",
        "date" : "2/10/2022",
        "temperature" : "29° celcius"
    }
]

@app.route('/temp', methods = ['GET'])
def displayTemp():

    return jsonify(temp)

@app.route('/temp', methods=['POST'])
def addTemp():
    temperature = request.get_json()
    temp.append(temperature)
    return {'id': len(temp)},200

    
@app.route('/temp/<int:index>', methods=['DELETE'])
def deleteTemp(index):
    temp.pop(index)
    return 'Temperature data was successfully deleted', 200


if __name__ == '__main__':

    app.run()


