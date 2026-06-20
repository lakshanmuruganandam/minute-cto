from pydantic import BaseModel, Field

class Requirements(BaseModel):
    product_description: str = Field(..., description="High level description of the product")
    target_users: int = Field(..., description="Expected scale of users")

class ArchitectureOutput(BaseModel):
    frontend: str
    backend: str
    database: str
    deployment: str
