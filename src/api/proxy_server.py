# src/api/proxy_server.py

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()


@app.get("/")
def root():
    return {"message": "✅ Proxy API đang hoạt động!"}


@app.get("/proxy/binance")
async def proxy_binance(symbol: str = Query(...)):
    url = "https://api.binance.com/api/v3/ticker/24hr"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Referer": "https://www.binance.com",
        "Origin": "https://www.binance.com"
    }
    params = {"symbol": symbol.upper()}

    try:
        async with httpx.AsyncClient(http2=True, timeout=10.0) as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return JSONResponse(content=response.json())
    except httpx.HTTPStatusError as e:
        return JSONResponse(
            content={
                "error": str(e),
                "url": str(e.request.url),
                "response": e.response.text
            },
            status_code=e.response.status_code
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Exception: {str(e)}"},
            status_code=500
        )


@app.get("/proxy/bybit")
async def proxy_bybit(category: str = Query(...), symbol: str = Query(...)):
    url = "https://api.bybit.com/v5/market/tickers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Referer": "https://www.bybit.com",
        "Origin": "https://www.bybit.com"
    }
    params = {"category": category, "symbol": symbol.upper()}

    try:
        async with httpx.AsyncClient(http2=True, timeout=10.0) as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return JSONResponse(content=response.json())
    except httpx.HTTPStatusError as e:
        return JSONResponse(
            content={
                "error": str(e),
                "url": str(e.request.url),
                "response": e.response.text
            },
            status_code=e.response.status_code
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Exception: {str(e)}"},
            status_code=500
        )
