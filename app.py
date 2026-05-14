from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
   
    # Extract numbers from the JSON body
    # Using .get(key, default) to prevent crashes if a key is missing
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
   
    # Simple addition logic
    total = num1 + num2
   
    # Return the result as a JSON object
    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": total
    })

if __name__ == '__main__':
    # Running on port 5000
    app.run(debug=True, port=5000)


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hello")
# def hello():
# 	return {"message": "Hello from Python"}
