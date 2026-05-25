from pydantic import BaseModel
from typing import List


class GenerateResponse(BaseModel):
    microsteps: List[str]