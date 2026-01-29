from pydantic import BaseModel,Field,field_validator
from typing import Annotated

class UserInput(BaseModel):
    proto: Annotated[str,Field(...,description="Protocol used (TCP, UDP, ICMP)")]
    state: Annotated[str,Field(...,description="Connection state")]
    flgs: Annotated[str,Field(...,description="TCP flags")]
    sport: Annotated[int,Field(...,description="Source port")]
    dport: Annotated[int,Field(...,description="Destination port")]
    pkts: Annotated[int,Field(...,description="Total packets") ]
    bytes: Annotated[int,Field(...,description="Total bytes")]
    dur: Annotated[float,Field(...,deprecated="Duration of connection")]
    spkts: Annotated[int,Field(...,description="Source packets")]
    dpkts: Annotated[int,Field(...,description="Destination packets")]
    sbytes: Annotated[int,Field(...,description="Bytes sent")]
    dbytes: Annotated[int,Field(...,description="Bytes received")]
    mean: Annotated[float,Field(...,description="Mean packet size")]
    stddev: Annotated[float,Field(...,description="Std deviation")]
    min: Annotated[float,Field(...,description="Minimum value")]
    max: Annotated[float,Field(...,description="Maximum value")]
    sum: Annotated[float,Field(...,description="Sum of values")]
    rate: Annotated[float,Field(...,description="Packet rate")]
    srate: Annotated[float,Field(...,description="Source rate")]
    drate: Annotated[float,Field(...,description="Destination rate")]
    
    @field_validator("proto", "state", "flgs", mode="before")
    @classmethod
    def force_string(cls, v):
        return str(v)
