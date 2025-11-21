from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from schemas import DemoRequest, DemoResponse

app = FastAPI(title="AI Health Assistant Site API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"ok": True, "service": "backend", "time": datetime.utcnow().isoformat()}


@app.post("/contact", response_model=DemoResponse)
def submit_contact(req: DemoRequest):
    # In real app, insert into DB or send email. For now, echo success.
    return DemoResponse(status="received", received_at=datetime.utcnow())


@app.get("/health")
def healthcheck():
    return {"status": "healthy", "time": datetime.utcnow().isoformat()} 
