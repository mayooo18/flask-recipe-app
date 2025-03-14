from flask import Flask, request, render_template
import requests
import os

apiLimit= 150 # 150 requests per day
apiCount = 0
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")


app = Flask(__name__)

def getRecipes(ingredients):
    global apiCount
    ingredients = ingredients.strip()
    if not ingredients:
        return [], 0, apiCount
    

    url=f"https://api.spoonacular.com/recipes/complexSearch?query={ingredients}&number=5&maxCalories=500&apiKey={SPOONACULAR_API_KEY}"

    
    try:
        response = requests.get(url, timeout=5)  # ✅ Timeout to prevent slow requests

        if response.status_code == 200:
            recipes = response.json().get("results", [])

            apiRemaining = int(response.headers.get("X-Ratelimit-Remaining", apiLimit - apiCount))
            apiCount += 5
            # checks if api limit is reached

            # ✅ Fetch full nutrition data for each recipe
            for recipe in recipes:
                recipe_id = recipe["id"]
                nutrition_url = f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json?apiKey={SPOONACULAR_API_KEY}"
                
                try:
                    nutrition_response = requests.get(nutrition_url, timeout=5)
                    if nutrition_response.status_code == 200:
                        recipe["nutrition"] = nutrition_response.json()
                    else:
                        recipe["nutrition"] = {}  # ✅ Set empty dictionary if nutrition fails

                except requests.exceptions.RequestException:
                    print(f"Failed to fetch nutrition for recipe ID: {recipe_id}")
                    recipe["nutrition"] = {}

            return recipes, apiRemaining, apiCount  # ✅ Return processed recipes and api count

        else:
            print(f"Error fetching recipes: {response.status_code}")
            return [], apiLimit - apiCount , apiCount

    except requests.exceptions.RequestException:
        print("Error: Could not connect to Spoonacular API.")
        return [], apiLimit - apiCount, apiCount
      

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    apiRemaining = apiLimit -apiCount
    apiUsed = apiCount

    if request.method== "POST":
        ingredients = request.form.get("ingredients")
        recipes, apiRemaining, apiUsed = getRecipes(ingredients)


    
    

    return render_template("index.html", recipes=recipes, apiRemaining=apiRemaining, apiUsed=apiUsed)
    



if __name__ == "__main__":
    app.run(debug=True)
    