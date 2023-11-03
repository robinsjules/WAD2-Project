from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from supabase import create_client

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

@app.route("/likepost", methods=['POST'])
def like_post():
        post_id = request.json.get('id')
        liked = request.json.get('liked')

        # If the post is liked, increment the likes; if unliked, decrement the likes
        if liked:
            supabase.table('Posts').update({'Likes': supabase.raw('Likes + 1')}).eq('id', post_id).execute()
        else:
            supabase.table('Posts').update({'Likes': supabase.raw('Likes - 1')}).eq('id', post_id).execute()

        return "Success", 200

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)