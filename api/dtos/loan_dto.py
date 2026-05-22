from pydantic import BaseModel
from core.validators import PositiveInt
from datetime import date

class LoanDto(BaseModel):
    book_id : PositiveInt
    requested_date : date
    n_days : date
