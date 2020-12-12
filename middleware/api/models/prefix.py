from pydantic import BaseModel


class PrefixSchema(BaseModel):
    id: int
    prefix: str
