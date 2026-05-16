from fastapi import FastAPI

app = FastAPI(title="Yusupov API")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
