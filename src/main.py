from fastapi import FastAPI
from src.routes.formulario import router as formulario_router
from fastapi.exceptions import RequestValidationError
from src.core.exception_handlers import validation_exception_handler
from fastapi.responses import RedirectResponse

app = FastAPI()
app.include_router(formulario_router)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
