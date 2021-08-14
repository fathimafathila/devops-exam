from pydantic import BaseModel


class CreateEmployeeRequest(BaseModel):
    first_name: str
    last_name: str
