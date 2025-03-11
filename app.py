import os
from google import genai
from dotenv import load_dotenv
from flask import Flask,request,jsonify
app=Flask(__name__)

load_dotenv()

api_key=os.getenv("API_KEY")
print(api_key)
client=genai.Client(api_key=api_key)

@app.route("/home",methods=['GET'])
def home():
    return"Hello world"

@app.route('/ai',methods=['POST'])
def ai():
    try:
        data=request.get_json()
        if 'prompt' not in data:
            return jsonify({
                "error":"Prompt not found in data"
            }),400
        prompt=data['prompt']
        response=client.models.generate_content(
           model="gemini-2.0-flash",
           contents=prompt
        )
        return jsonify({
            "ai_response":response.text
        }),200
    except Exception as e:
        return jsonify({
            "error":str(e)
        }),500
if(__name__)=='_main_':
    app.run(debug=True)
# print(response.text)
