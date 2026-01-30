from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from app.pinterest import download_pinterest

app = FastAPI(
    title="Pinterest Downloader API",
    description="Download Pinterest Videos & Images in High Quality",
    version="1.0"
)

@app.get("/")
def home():
    return {"status": "Pinterest Downloader API Running ✅"}

@app.get("/download")
def download(url: str = Query(..., description="Pinterest video/image link")):
    try:
        data = download_pinterest(url)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
