from dotenv import load_dotenv
from pydantic import Field
from functools import lru_cache
from google.cloud import firestore
from google.oauth2 import service_account
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings
load_dotenv()


class Settings(BaseSettings):
    secret_key: str = Field("SECRET_KEY")
    google_application_credentials: dict = Field("GOOGLE_APPLICATION_CREDENTIALS")


settings = Settings()
app = FastAPI(title="⚡ ZapStore")
credentials = service_account.Credentials.from_service_account_info(settings.google_application_credentials)
db = firestore.Client(credentials=credentials, project=credentials.project_id)
origins = ["http://localhost:8000", "https://spiritualtours.web.app", "https://spiritualtours.com"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@lru_cache
def verify_secret(x_secret: str = Header(...)):
    if x_secret != settings.secret_key:
        raise HTTPException(status_code=412, detail="Invalid or missing secret")

# POST endpoint: create new document in given collection
@app.post("/collections/{collection_name}")
async def create_item(collection_name: str, item: dict, dep: None = Depends(verify_secret)):
    try:
        doc_ref = db.collection(collection_name).add(item)  # auto-ID
        return {"message": "Document created successfully", "id": doc_ref[1].id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET endpoint: fetch all documents from given collection
@app.get("/collections/{collection_name}")
async def get_items(collection_name: str, dep: None = Depends(verify_secret)):
    try:
        docs = db.collection(collection_name).stream()
        items = [{**doc.to_dict(), "id": doc.id} for doc in docs]
        return {"count": len(items), "items": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
