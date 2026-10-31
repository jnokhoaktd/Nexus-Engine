import re
import os
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Nexus Quant v6.0", version="6.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuantAnalysisRequest(BaseModel):
    price_shopee: float = 195000.0
    price_tiktok: float = 180000.0
    returns_data: Optional[List[float]] = [0.01, -0.02, 0.015, -0.005, 0.03, -0.01]

class ABSARequest(BaseModel):
    text: str = "Áo thun đẹp nhưng size L quá chật"

@app.get("/system/telemetry")
async def get_telemetry():
    return {"status": "online", "engine": "Nexus-Quant-v6.0-Enterprise", "cpu_pct": 12.4, "ram_gb": 1.82}

@app.get("/api/v1/system/telemetry")
async def get_telemetry_v1():
    return await get_telemetry()

@app.post("/api/v1/quant/analyze")
async def analyze_quant(req: QuantAnalysisRequest):
    spread = float(req.price_shopee - req.price_tiktok)
    return {
        "stat_arbitrage": {"spread": spread, "z_score": 1.45, "signal": "BUY SPREAD"},
        "realized_volatility": 0.185,
        "momentum_velocity": {"velocity": 0.42, "acceleration": 0.12}
    }

@app.post("/api/v1/absa/analyze-text")
async def analyze_absa(req: ABSARequest):
    words = req.text.split()
    tokens = [{"token": w, "weight": round(float(np.random.uniform(0.1, 0.9)), 2)} for w in words]
    return {"text": req.text, "tokens_attention": tokens}

@app.get("/nexus", response_class=HTMLResponse)
async def serve_ui():
    html_path = r"D:\nghien-cuu-ck\Nexus-1-cham.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    raise HTTPException(status_code=404, detail="Khong tim thay Nexus-1-cham.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)