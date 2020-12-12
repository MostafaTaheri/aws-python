from pydantic import BaseModel


class UserPrefixSchema(BaseModel):
    user_id: int
    prefix_id: int
    is_allowed: int
