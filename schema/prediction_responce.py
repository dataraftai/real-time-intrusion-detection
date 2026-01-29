from pydantic import BaseModel,Field

class predictionResponce(BaseModel):

    predicted_category : int = Field(...,description="0 = Normal, 1 = Intrusion")
    confidence: float = Field(
        ..., description="Probability of intrusion"
    )
