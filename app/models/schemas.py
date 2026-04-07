from pydantic import BaseModel

class TradeRequest(BaseModel):
    trade_id: str
    asset: str
    volume: float
    price: float
    trader: str
    timestamp: str

class ComplianceResponse(BaseModel):
    analysis: str
    sources: list
