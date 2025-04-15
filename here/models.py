# generated by fastapi-codegen:
#   filename:  shadowed_imports.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from datetime import date as date_aliased
from typing import Optional

from pydantic import BaseModel, Field


class MarketingOptIn(BaseModel):
    optedIn: Optional[bool] = Field(None, example=False)
    date: Optional[date_aliased] = Field(None, example='2018-04-26T17:03:25.155Z')
