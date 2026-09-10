from ipaddress import IPv4Address, IPv6Address 
from pydantic import BaseModel, Field


class Target(BaseModel):
    
    hostName: str | None = None
    ipv4: IPv4Address | None = None
    ipv6: IPv6Address | None = None
    ports: list[int] = Field(default_factory=list)