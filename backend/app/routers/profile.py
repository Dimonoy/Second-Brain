from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header

router = APIRouter(
    prefix='/profile',
    tags=['profile'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not Found'}}
)


@router.get('/')
async def get_profile():
    return {}
