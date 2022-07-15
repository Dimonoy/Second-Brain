from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header

router = APIRouter(
    prefix='/pages',
    tags=['pages'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not Found'}}
)

@router.get('/')
async def get_pages():
    return {}

@router.get('/{page_id}')
async def get_page():
    return {}
