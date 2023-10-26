from flask import Flask, jsonify
import os
from supabase import create_client, Client
from flask_cors import CORS
import logging
import requests

app = Flask(__name__)
CORS(app)

# url: str = os.environ.get("https://mpdbdcytohoflyionlyn.supabase.co")
# key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1wZGJkY3l0b2hvZmx5aW9ubHluIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc2MTAyNTIsImV4cCI6MjAxMzE4NjI1Mn0.1tKz3KYVupIppWbWLx3HMKi87CnZlrpqk1Ehht-Rb6c")
# supabase: Client = create_client(url, key)
# logger = logging.getLogger(__name__)

spoonacularAPIKey = 'd0306a1f1a9b4bc39936a08452767153'

# @app.route("/AllRecipes", methods=['GET'])
# def getAllRecipes():
#     recipes = supabase.table('Recipes').select('*').execute()
#     return jsonify(recipes['data'])

recipeQuery = "pasta" # test

@app.route("/AllRecipes", methods=['GET', 'POST'])
def getAllRecipes(recipeQuery):
    recipes = requests.get(f"https://api.spoonacular.com/recipes/search?query={recipeQuery}&apiKey={spoonacularAPIKey}&number=10")
    return jsonify(recipes)