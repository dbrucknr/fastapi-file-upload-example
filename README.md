# Running the API:

- `source .venv/bin/activate`
- `uvicorn src.main:api --reload`

## Steps I took to Create the Api

1. `uv init`
2. `uv add fastapi uvloop uvicorn httptools orjson pydantic python-multipart`
3. `source .venv/bin/activate`
4. `mkdir src`
5. `touch src/main.py`
