from flask import Flask,request
from flask_cors import CORS,cross_origin
from transformers import AutoModel,AutoTokenizer
import torch
import json
#from peft import PeftModel

app = Flask(__name__)

CORS(app)

#model = AutoModel.from_pretrained("/root/projects/zhj/chatGLM_6B", trust_remote_code=True, load_in_8bit=True, device_map='auto')
#tokenizer = AutoTokenizer.from_pretrained("/root/projects/zhj/chatGLM_6B", trust_remote_code=True)
#model = PeftModel.from_pretrained(model, "/root/projects/zhj/ChatGLM-Tuning/output/")
total_history=[]

@app.route('/')
def index():
    return 'hello chatGLM'

@app.route('/chat', methods=['POST'])
@cross_origin(supports_credentials=True)
def chat():
    global total_history
    input_text = request.get_json()['message']
    #response, history = model.chat(tokenizer, input_text, history=total_history)
    history = []
    total_history += history
    response = '这是一条回复'
    return json.dumps({'data':response})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
