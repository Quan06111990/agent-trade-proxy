from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/proxy/binance")
async def proxy_binance(symbol: str = Query(...)):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/proxy/bybit")
async def proxy_bybit(symbol: str = Query(...)):
    url = f"https://api.bybit.com/v5/market/tickers?category=linear&symbol={symbol.upper()}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
