from flask import Flask, request, jsonify
from all_interface_polish import AllCheckerGUI
import subprocess

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_urls():
    # Get URL from request body
    url = request.json['url']
    # Create AllChecker object and run
    checker = AllCheckerGUI(url)
    checker.run()
    # Return response with output from AllChecker
    response = {'onlineURLs': checker.onlineURLs, 'offlineURLs': checker.offlineURLs}
    return jsonify(response)

@app.route('/launch', methods=['GET'])
def launch_gui():
    # Launch GUI using subprocess module
    subprocess.Popen(['python', 'all_interface_polish.py'])
    return jsonify({'message': 'GUI launched'})

if __name__ == '__main__':
    app.run(debug=True)
