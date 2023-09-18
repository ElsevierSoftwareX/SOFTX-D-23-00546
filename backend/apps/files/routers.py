import datetime
import os
from typing import List

import pydantic
from bson import ObjectId
from fastapi import APIRouter, File, HTTPException, Request, UploadFile, status
from fastapi.responses import JSONResponse

from .textpreprocessing.process import process
from .morpheme.inference import inference

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str
router = APIRouter()


# POST: upload multiple .txt files =============================
@router.post("/korcat")
async def upload_files(request: Request, files: List[UploadFile] = File(...)):
    cnt = 100

    # make object for each file uploaded 
    for file in files:
        contents = await file.read()

        print(file.filename)
        print(contents.decode('UTF8'))

		# process the uploaded text
        results = process(contents.decode('UTF8'))

		# each object being uploaded to MONGODB
        upload = {
            "_id": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + "-C" + str(cnt),
            "filename": file.filename,
            "contents": contents,
            "results": results
        }
        cnt += 1

        new_file = await request.app.mongodb["korcat"].insert_one(upload)
        created_file = await request.app.mongodb["korcat"].find_one({"_id": new_file.inserted_id})

    return {"filenames": [file.filename for file in files]}


@router.post("/morpheme")
async def upload_files(request: Request, files: List[UploadFile] = File(...)):
    cnt = 100

    # make object for each file uploaded 
    for file in files:
        contents = await file.read()

        print(file.filename)
        print(contents.decode('UTF8'))

		# process the uploaded text
        results = inference(contents.decode('UTF8'))

		# each object being uploaded to MONGODB
        upload = {
            "_id": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + "-M" + str(cnt),
            "filename": file.filename,
            "contents": contents,
            "results": results
        }
        cnt += 1

        new_file = await request.app.mongodb["morpheme"].insert_one(upload)
        created_file = await request.app.mongodb["morpheme"].find_one({"_id": new_file.inserted_id})

    return {"filenames": [file.filename for file in files]}


# GET: list all files; list file by ID =========================
@router.get("/korcat", response_description="List all files")
async def list_files(request: Request):
    files = []

    for doc in await request.app.mongodb["korcat"].find().to_list(length=100):
        files.append(doc)
    return files


@router.get("/morpheme", response_description="List all files")
async def list_files(request: Request):
    files = []

    for doc in await request.app.mongodb["morpheme"].find().to_list(length=100):
        files.append(doc)
    return files


@router.get("/korcat/{id}", response_description="Get a single file")
async def show_file(id: str, request: Request):
    if (file := await request.app.mongodb["korcat"].find_one({"_id": id})) is not None:
        return file

    raise HTTPException(status_code=404, detail=f"File {id} not found")


@router.get("/morpheme/{id}", response_description="Get a single file")
async def show_file(id: str, request: Request):
    if (file := await request.app.mongodb["morpheme"].find_one({"_id": id})) is not None:
        return file

    raise HTTPException(status_code=404, detail=f"File {id} not found")


# delete file by ID ============================================
@router.delete("/korcat/{id}", response_description="Delete file")
async def delete_file(id: str, request: Request):
    delete_result = await request.app.mongodb["korcat"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


# delete file by ID ============================================
@router.delete("/morpheme/{id}", response_description="Delete file")
async def delete_file(id: str, request: Request):
    delete_result = await request.app.mongodb["morpheme"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Task {id} not found")
