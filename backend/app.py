from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)

url = "https://mpdbdcytohoflyionlyn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1wZGJkY3l0b2hvZmx5aW9ubHluIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc2MTAyNTIsImV4cCI6MjAxMzE4NjI1Mn0.1tKz3KYVupIppWbWLx3HMKi87CnZlrpqk1Ehht-Rb6c"
supabase = create_client(url, key)

# code works
@app.route("/users", methods=['GET'])
def getAllUsers():
    response = supabase.table('Users').select('*').execute()
    return(response.data)

# code in progress -> Add users for when they register
@app.route("/add_users", methods=['POST'])
def addUsers():
    try:
        data = request.json  # Assuming the client sends a JSON object with user data

        # Insert data into the Users table
        response = supabase.table('Users').upsert(data, ['Email'])  # Assuming 'Email' is the primary key

        if response['status_code'] == 200:
            return jsonify({"message": "User added successfully"})
        else:
            return jsonify({"error": "Failed to add user"})

    except Exception as e:
        return jsonify({"error": str(e)})

# code works   
@app.route('/get_profile/<username>', methods=['GET'])
def get_profile(username):
    print(f"Received request for username: {username}")
    response = supabase.table('Users').select('*').eq('UserName', username).execute()
    return (response.data)
    
# code in progress -> Route to update user data by username
@app.route('/update_profile/<username>', methods=['POST','PUT'])
def update_user(userName):
    try:
        data = request.json  # Assuming the client sends a JSON object with updated user data

        # Update data in the Users table based on the specified email
        response = supabase.table('Users').update(data, ['UserName'], condition=f'UserName.eq.{userName}')

        if response['status_code'] == 200:
            return jsonify({"message": "User updated successfully"})
        else:
            return jsonify({"error": "Failed to update user"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)