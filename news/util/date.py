from datetime import datetime
from ..values.common import DATE_FORMAT

def today() -> str:
    return datetime.today().strftime(DATE_FORMAT)
