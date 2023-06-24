import logging

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


class ApiBaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, status_code=500, detail=None) -> None:
        self.status_code = status_code
        self.detail = detail
        if self.detail:

            logging.exception(self.detail)


class EnvironmentException(ApiBaseException):
    status_code = 400

    def __init__(self, detail=None) -> None:
        self.detail = detail
        ApiBaseException.__init__(
            self, status_code=self.status_code, detail=self.detail
        )


class BusinessException(ApiBaseException):
    status_code = 400

    def __init__(self, detail=None) -> None:
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class NotFoundException(ApiBaseException):
    status_code = 404

    def __init__(self, detail=None) -> None:
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class UnprocessableEntityException(ApiBaseException):
    status_code = 422

    def __init__(self, detail=None) -> None:
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class GitException(ApiBaseException):
    status_code = 500

    def __init__(self, detail=None) -> None:
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)

class ComparatorNotExists(ApiBaseException):
    status_code = 422

    def __init__(self, detail=None) -> None:
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)

class BadRequestException(ApiBaseException):
    status_code = 400

    def __init__(self, detail=None) -> None:
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class MissingSessionError(Exception):
    """Excetion raised for when the user tries to access a database session before it is created."""

    def __init__(self):
        msg = """
        No session found!
            db.session.query(User).all()
        """

        super().__init__(msg)

def generic_handler(_: Request, exception: ApiBaseException):
    return JSONResponse(
        status_code=exception.status_code, content={"detail": exception.detail}
    )


def on_auth_error(_: Request):
    return JSONResponse(
        status_code=401,
        content={"detail": "Não autorizado, token inválido ou inexistente"},
    )


async def database_handler(exception: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
