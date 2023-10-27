from flask import Flask
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)

url = "insert supabase url here"
key = "insert supabase key here"
supabase = create_client(url, key)

@app.route("/users", methods=['GET'])
def getAllUsers():
    response = supabase.table('Users').select('*').execute()
    return(response.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)