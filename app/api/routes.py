from fastapi import APIRouter
from app.models.schemas import TradeRequest, ComplianceResponse
from app.services.compliance_engine import analyze_trade

router = APIRouter()

@router.post("/analyze", response_model=ComplianceResponse)
def analyze_trade_route(trade: TradeRequest):
    result = analyze_trade(trade.dict())
    return result
