from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.requests import Request
import uvicorn

from api import employee
import models

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/employees')
def get_employees(lite: bool=True):
    return JSONResponse(employee.get_employees(lite))


@app.post('/employees')
def create_employee(request: models.CreateEmployeeRequest):
    data = request.dict()

    response = employee.create_employee(data)

    return JSONResponse(response)


@app.get('/employee/{employee_id}')
def get_emplyee_info(employee_id: str):
    response = employee.get_emplyee_info(employee_id)

    return JSONResponse(response)

#add
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=4000)
