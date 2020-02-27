import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8004)
