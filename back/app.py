from flask import Flask, request
from flask_cors import CORS

from datetime import datetime, date, time, timezone

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/time',methods=["POST"])
def time():
    zone = int(request.json['zone'])
    print(datetime.now()) 
    gmttime = datetime.now(timezone.utc).strftime("%I:%M%p")
    gmtminute = datetime.now(timezone.utc).strftime("%M")
    gmthour = datetime.now(timezone.utc).strftime("%I")
    tag = datetime.now(timezone.utc).strftime("%p")
    print('hour')
    print(gmthour) 
    print('time')
    print(gmttime)
   
    newhour = int(gmthour) + zone 
    if newhour > 12 or newhour < 0:
      if tag == "pm":
        tag == "am"
      elif tag == "am":
        tag == "pm"
    if newhour > 12: 
      newhour = newhour - 12
    elif newhour < 0:
      newhour = newhour + 12
    
    returntime = str(newhour) + ":" + gmtminute + tag

    return {'time': returntime}
   
if __name__ == "__main__":
    app.run()
