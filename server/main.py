from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = FastAPI()  # Change variable name to 'app'

@app.get("/test")
async def root():
    return {"msg": "API is Online"}

if __name__ == "__main__":
    # Print to debug if APP_ENV is being loaded
    print("App Environment:", os.environ.get('APP_ENV'))

    if os.environ.get('APP_ENV') == "development":
        print("Starting Uvicorn in development mode...")
        uvicorn.run("main:app", host="0.0.0.0", port=3500, workers=4, reload=True)
    else:
        print("App is not in development mode. Skipping Uvicorn.")
