from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MetricCreate(BaseModel):
    host: str
    cpu_percent: Optional[float] = None
    cpu_min: Optional[float] = None
    cpu_max: Optional[float] = None
    memory_percent: Optional[float] = None
    memory_min: Optional[float] = None
    memory_max: Optional[float] = None
    disk_percent: Optional[float] = None
    disk_min: Optional[float] = None
    disk_max: Optional[float] = None
    network_in: Optional[int] = None
    network_out: Optional[int] = None
    timestamp: Optional[datetime] = None


class MetricResponse(BaseModel):
    timestamp: datetime
    host: str
    cpu_percent: Optional[float] = None
    cpu_min: Optional[float] = None
    cpu_max: Optional[float] = None
    memory_percent: Optional[float] = None
    memory_min: Optional[float] = None
    memory_max: Optional[float] = None
    disk_percent: Optional[float] = None
    disk_min: Optional[float] = None
    disk_max: Optional[float] = None
    network_in: Optional[int] = None
    network_out: Optional[int] = None

    class Config:
        from_attributes = True

class AlertResponse(BaseModel):
    id: int
    timestamp: datetime
    host: str
    metric_type: str
    severity: str
    message: Optional[str] = None
    status: str

    class Config:
        from_attributes = True


class AlertUpdate(BaseModel):
    status: str

