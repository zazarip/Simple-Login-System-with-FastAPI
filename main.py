from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
import sqlite3

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authenticate user function
def authenticate_user(username: str, password: str):
    conn = sqlite3.connect('database/login_database.db')
    cursor = conn.cursor()

    # Fetch user record from the database
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    conn.close()
    return user

# Login endpoint
@app.post("/login")
async def login(username: str, password: str):
    user = authenticate_user(username, password)

    if user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Login failed")



