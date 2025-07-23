# src/api/proxy_server.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "✅ Agent Trade Proxy is running!"}

@app.get("/proxy/binance")
async def proxy_binance(symbol: str = Query(...)):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            return JSONResponse(content=response.json())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/proxy/bybit")
async def proxy_bybit(symbol: str = Query(...)):
    url = f"https://api.bybit.com/v2/public/tickers?symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            return JSONResponse(content=response.json())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
