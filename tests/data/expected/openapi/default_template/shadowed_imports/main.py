# generated by fastapi-codegen:
#   filename:  shadowed_imports.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(
    title='REST API',
    version='0.0.1',
    servers=[{'url': 'https://api.something.com/1'}],
)
