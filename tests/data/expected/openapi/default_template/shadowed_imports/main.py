# generated by fastapi-codegen:
#   filename:  shadowed_imports.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from datetime import date as date_aliased
from typing import Optional

from fastapi import FastAPI

app = FastAPI(
    title='REST API',
    version='0.0.1',
    servers=[{'url': 'https://api.something.com/1'}],
)


@app.get('/actions/', response_model=None)
def get_actions_(due: Optional[date_aliased] = None) -> None:
    pass
