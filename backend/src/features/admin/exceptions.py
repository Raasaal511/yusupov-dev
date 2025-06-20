from fastapi import HTTPException


class AdminNotFoundError(HTTPException, Exception):
    ...