from typing import Annotated

from pydantic import BaseModel, StringConstraints


class UserModel(BaseModel):
    username: Annotated[str, StringConstraints(min_length=1, strip_whitespace=True)]
    password: Annotated[str, StringConstraints(min_length=1, strip_whitespace=True)]
