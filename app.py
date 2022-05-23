from flask import Flask, request
import requests
import json
import config

app = Flask(__name__)
app.config['SECRET_KEY'] ='547dgfgfg-34464h-teteyeb'

def callSendAPI(senderPsid, response):
  PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN
  payload = {
    'recipient':{'id':senderPsid},
    'message':response,
    'messaging_type':'RESPONSE'
  }
headers = {'content-type':'application/json'}
@app.route('/', methods = ["GET", "POST"])
def home():
  return 'HOME'

def handleMessage(senderPsid, recievedMessage):
  if 'text' in recievedMessage:
    response = {"text": 'You sent me :{}'.format(recievedMessage['text'])}
    callSendAPI(senderPsid, response)
     
  else:
    response = {"text: 'This chatbot only accepts text messages"}
    callSendAPI(senderPsid, response)
                

@app.route('/webhook', methods=["GET", "POST"])
def index():
  VERIFY_TOKEN = "hello"
  
  if request.method =="POST":
    VERIFY_TOKEN = "hello"
    
  if 'hub.mode' in request.args:
    mode = request.args.get('hub.mode')
    print(mode)
  if 'hub.verify_token' in request.args:
    token = request.args.get('hub.verify_token')
    print(token)
  if 'hub.challenge' in request.args:
    challenge = request.args.get('hub.challenge')
    print(challenge)
  if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    
  if mode =='subscribe' and token==VERIFY_TOKEN:
    print('WEBHOOK VERIFIED')
    
    challenge = request.args.get('hub.challenge')
    return challenge, 200
  else:
    return 'ERROR', 403
#return 'SOMETHING', 200


  if request.method =="POST":
    VERIFY_TOKEN = "hello"
  if 'hub.mode' in request.args:
    mode = request.args.get('hub.mode')
    print(mode)
  if 'hub.verify_token' in request.args:
    token = request.args.get('hub.verify_token')
    print(token)
  if 'hub.challenge' in request.args:
    challenge = request.args.get('hub.challenge')
    print(challenge)
  if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    
    if mode =='subscribe' and token==VERIFY_TOKEN:
       print('WEBHOOK VERIFIED')
       challenge = request.args.get('hub.challenge')
       return challenge, 200
    else:
      return 'ERROR', 403
    
    data = request.data
    body = json.loads(data.decode('utf-8'))
    if 'object' in body and body['object']=='page':
        entries = body['entry']
        for entry in entries:
          webhookEvent = entry['messaging'][0]
          print(webhookEvent)
          senderPsid = webhookEvent['sender']['id']
          print('Sender PSID:{}'.format(senderPsid))
          
          if 'message' in webhookEvent:
            handleMessage(senderPsid, webhookEvent['message'])
          return 'EVENT_RECIEVED', 200
    else:
      return 'ERROR', 404
            

if __name__=='__main__':
            app.run(host ='0.0.0.0', port='1337', debug=True)
            
            
      
