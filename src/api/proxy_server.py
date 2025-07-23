# src/api/proxy_server.py

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "✅ Proxy API đang hoạt động!"}

@app.get("/proxy/binance")
async def proxy_binance(symbol: str = Query(...)):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/proxy/bybit")
async def proxy_bybit(
    category: str = Query(default="linear"),
    symbol: str = Query(default="BTCUSDT")
):
    url = f"https://api.bybit.com/v5/market/tickers?category={category}&symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
