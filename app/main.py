from fastapi import FastAPI

app = FastAPI(
    title="Employee Task Management API",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Employee Task Management API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}