from flask import Flask
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)

url = "https://mpdbdcytohoflyionlyn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1wZGJkY3l0b2hvZmx5aW9ubHluIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc2MTAyNTIsImV4cCI6MjAxMzE4NjI1Mn0.1tKz3KYVupIppWbWLx3HMKi87CnZlrpqk1Ehht-Rb6c"
supabase = create_client(url, key)

@app.route("/users", methods=['GET'])
def getAllUsers():
    response = supabase.table('Users').select('*').execute()
    return(response.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)