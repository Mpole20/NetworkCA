from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>NetworkCA Project</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    max-width: 800px; 
                    margin: 0 auto; 
                    padding: 20px; 
                    background: #f5f5f5;
                }
                .container { 
                    background: white; 
                    padding: 30px; 
                    border-radius: 10px; 
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1> Cloud Deployment </h1>
                <p>This Python Flask app is running in Docker on AWS ECS</p>
                <p><strong>Technology Stack:</strong></p>
                <ul>
                    <li>Python Flask</li>
                    <li>Docker</li>
                    <li>Terraform</li>
                    <li>AWS ECS Fargate</li>
                    <li>GitHub Actions CI/CD</li>
                </ul>
            </div>
        </body>
    </html>
    '''



if __name__ == '__main__':
    print("Starting Flask server on port 3000...")
    app.run(host='0.0.0.0', port=3000, debug=False)