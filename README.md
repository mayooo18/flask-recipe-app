#Flask Recipe Finder  

A simple **Flask web app** that suggests recipes based on user-input ingredients using the **Spoonacular API**. It **tracks API requests globally** and **resets daily** to stay within the **150-request limit**.

---

## Features  
- Find recipes by entering ingredients  
- See nutrition facts (calories, protein, carbs, fat)  
- Tracks API requests (shared across all users)  
- Automatically resets daily at midnight  
- Styled with HTML & CSS for a clean UI  
- Deployed on Render  

---

## Tech Stack  
- **Python** (Flask) – Backend API handling  
- **HTML/CSS** – Frontend styling  
- **Spoonacular API** – Fetches recipes & nutrition info  
- **Requests Library** – Handles API calls  
- **Render** – Deployment  
- **Git & GitHub** – Version control  

---

## Installation  

### 1. Clone the Repository  
```sh
git clone https://github.com/mayooo18/flask-recipe-app.git
cd flask-recipe-app
```

### 2. Create a Virtual Environment  
```sh
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables  
Create a `.env` file and add:  
```sh
SPOONACULAR_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your **Spoonacular API key**.

---

## Running the App  
Start the Flask server:  
```sh
python app.py
```
Visit: `http://127.0.0.1:5000` in your browser.

---

## Live Demo  
The app is deployed on Render:  
[Live App](https://flask-recipe-app.onrender.com/)

---

## How API Request Tracking Works  
- **Shared for all users** – If someone uses a request, it reduces for everyone.  
- **Persists across restarts** – Stored in `api_count.txt` to avoid reset.  
- **Resets daily** at midnight (based on system time).  

---

## Customization  
- **Change UI colors** – Edit `index.html` CSS styles.  
- **Increase API requests** – Upgrade your Spoonacular plan.    
