"""
Функции друг на друга ссылаются
Поэтому get_me(user: User = Depends(get_user_by_auth_token))
В Swagger уже отображается с auth-token, который требуется ввести в заголовок запроса!!!

"""

from fastapi import HTTPException, status, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_async import get_session
from . import crud
from models import User


# ... - значение обязательно
# Функция get_user_by_auth_token завист от передачи в неё токена token
async def get_user_by_auth_token(
    token: str = Header(..., alias="x-auth-token"),
    session: AsyncSession = Depends(get_session),
) -> User:
    user: User | None = await crud.get_user_by_token(
        session=session,
        token=token,
    )
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Auth token invalid!"
        )
