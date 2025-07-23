from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "✅ Proxy API đang hoạt động!"}

@app.get("/proxy/binance")
async def proxy_binance(symbol: str = Query(...)):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            return response.json()
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
