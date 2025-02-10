from flask import Flask, request, render_template
import requests

SPOONACULAR_API_KEY = "8ddbbd75ed2c403c99f24d96abbb75e6"
app = Flask(__name__)

def getRecipes(ingredients):
    ingredients = ingredients.strip()

    url=f"https://api.spoonacular.com/recipes/complexSearch?query={ingredients}&number=5&maxCalories=500&apiKey={SPOONACULAR_API_KEY}"

    
    try:
        response = requests.get(url, timeout=5)  # ✅ Timeout to prevent slow requests

        if response.status_code == 200:
            recipes = response.json().get("results", [])

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

            return recipes  # ✅ Return processed recipes

        else:
            print(f"Error fetching recipes: {response.status_code}")
            return []

    except requests.exceptions.RequestException:
        print("Error: Could not connect to Spoonacular API.")
        return []
      

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    if request.method== "POST":
        ingredients = request.form.get("ingredients")
        recipes = getRecipes(ingredients)
    
    

    return render_template("index.html", recipes=recipes)
    



if __name__ == "__main__":
    app.run(debug=True)