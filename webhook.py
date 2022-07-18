from flask import Flask, request, Response
import requests
app = Flask(__name__)
@app.route('/my_webhook', methods=['POST'])
def return_response():
    print(request.json);
    meraki_request = requests.post(url="https://uat-everstreamemployeecentral.cs69.force.com/services/apexrest/webhooks/NMSEndpoint/handleAlert", data=request.json, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(meraki_request)
    return Response(status=200)
if __name__ == "__main__": app.run()