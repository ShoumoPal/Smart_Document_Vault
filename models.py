from database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from typing import Optional

class VaultDB(Base):
    __tablename__ = 'docvault'
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    summary = Column(String)
    tags = Column(String)

class CreateVaultItem(BaseModel):
    summary : str
    filename : str
    tags : str

class VaultItem(CreateVaultItem):
    id : Optional[int] = None
    class Config:
        orm_mode = True