from pydantic import BaseModel,Field

class predictionResponce(BaseModel):

    predicted_category : int = Field(...,description="0 = Normal, 1 = Intrusion")
    traffic_type :str = Field(...,description="label")
    confidence: float = Field(
        ..., description="Probability of intrusion"
    )
    decision_threshold : float