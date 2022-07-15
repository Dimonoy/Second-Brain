from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header

router = APIRouter(
    prefix='/settings',
    tags=['settings'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not Found'}}
)


@router.get('/')
async def get_settings():
    return {}

@router.put('/update/')
async def update_settings():
    return {}

@router.delete('/delete/')
async def delete_settings():
    return {}
