from fastapi import FastAPI

app = FastAPI(
    title="Resume AI API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Resume AI Backend Running"
    }