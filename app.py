from fastapi import FastAPI, HTTPException

app = FastAPI()

correct_pass = "20052026"

@app.get("/")
def home():
    return {"message": "Color Trading App Running Successfully"}

@app.get("/login")
def login(passcode: str):
    if passcode == correct_pass:
        return {"status": "Success", "message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Wrong password")

@app.get("/predict")
def predict():
    return {
        "big_small": "BIG",
        "color": "RED",
        "sure_chance": "95%"
    }
