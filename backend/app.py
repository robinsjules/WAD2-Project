from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from supabase import create_client
import base64

app = Flask(__name__)
CORS(app)

url = "https://mpdbdcytohoflyionlyn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1wZGJkY3l0b2hvZmx5aW9ubHluIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc2MTAyNTIsImV4cCI6MjAxMzE4NjI1Mn0.1tKz3KYVupIppWbWLx3HMKi87CnZlrpqk1Ehht-Rb6c"
supabase = create_client(url, key)

# code works -> get all users in data base
@app.route("/users", methods=['GET'])
def getAllUsers():
    response = supabase.table('Users').select('*').execute()
    return(response.data)

# code works -> add user data to the database after they register
@app.route("/register_user", methods=['POST'])
def registerUsers():
    data = request.json
    response = supabase.table('Users').insert(data).execute()
    return (response.data)

@app.route("/sign_up", methods=['POST'])
def sign_up():
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        return jsonify({'message': 'Authorization header is missing'}), 401
    if not auth_header.startswith('Basic'):
        return jsonify({'message': 'Invalid Authorization header format'}), 401
    credentials = auth_header[len('Basic '):]
    decoded_credentials = base64.b64decode(credentials).decode('utf-8')
    email, password = decoded_credentials.split(':')
    signUp = supabase.auth.sign_up(email, password)
    return jsonify({'userId': signUp.user.id, "access_token": signUp.session.access_token, "refresh_token": signUp.session.refresh_token})

# @app.route("/retrieve_session")
# def retrieve_session():
#     session = supabase.auth.get_session()
#     email = session.user.email if session else None
#     if email:
#         user = supabase.table('Users').select("*").eq('Email', email).execute()
#         if user.get('data'):
#             user_data = user.get('data')[0]
#             return jsonify({'username': user_data['UserName'], 'email': email})
    
#     return jsonify({'error': 'No session found'})

# @app.route("/refresh_session", methods=['GET'])
# def refresh_session():
#     supabase = create_client(url, key)
#     session = supabase.auth.get_session()
#     if session is not None:
#         return jsonify({'email': session.user.email, "access_token": session.access_token, "refresh_token": session.refresh_token})

# code works -> hooooooray can only log in if u are an authorised user on supabase     
@app.route("/auth_sign_in", methods=['POST'])
def sign_in():
    auth_header = request.headers.get('Authorization')

    if auth_header is None or not auth_header.startswith('Basic'):
        return jsonify({'message': 'Invalid or missing Authorization header'}), 401

    credentials = auth_header[len('Basic '):]
    decoded_credentials = base64.b64decode(credentials).decode('utf-8')
    email, password = decoded_credentials.split(':')

    try:
        session = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return jsonify({
            'email': session.user.email,
            'access_token': session.session.access_token,
            'refresh_token': session.session.refresh_token
        }), 200
    except Exception as e:
        return jsonify({'message': 'Authentication failed', 'error': str(e)}), 401


@app.route("/auth_sign_out")
def sign_out():
    res = supabase.auth.sign_out()
    return jsonify({'message': 'Signed out'}), 200

# code works -> get profile of user
@app.route('/get_profile/<username>', methods=['GET'])
def get_profile(username):
    response = supabase.table('Users').select('*').eq('UserName', username).execute()
    return (response.data)

# code works -> update profile of user
@app.route("/update_profile/<username1>", methods=['POST', 'PUT'])
def update_user(username1):
    data = request.json
    response = supabase.table('Users').update(data).eq('UserName', username1).execute()
    return (response.data)

# code works -> get posts
@app.route("/communityposts", methods=['GET'])
def get_communityposts():
    response = supabase.table('Posts').select('*').execute()
    return (response.data)

@app.route("/post_to_community", methods=['POST'])
def post_to_community():
    data = request.json
    response = supabase.table('Posts').insert(data).execute()
    return (response.data)

# code works -> like post
@app.route("/likepost", methods=['PUT'])
def like_post():
    data = request.json
    postid = data.get('id')
    likes = data.get('likes')

    if postid is not None and likes is not None:
        response = supabase.table('Posts').update({'Likes': likes}).eq('id', postid).execute()

    return (response.data)

@app.route("/listings", methods=['GET'])
def getListings():
    response = supabase.table("SurplusListings").select("*").execute()
    return response.data

@app.route("/add_listing", methods=['POST'])
def addSurplusListing():
    data = request.json
    response = supabase.table("SurplusListings").insert(data).execute()
    # return Response((response.data),mimetype="application/json")
    return (response.data)

@app.route("/add_recipe", methods=['POST'])
def testAdd():
    data = request.json
    response = supabase.table("Tes3").insert(data).execute()
    return (response.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)