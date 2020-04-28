import datetime as datetimes
from datetime import date, datetime
from app.Extensions import db
from app.Kit import (Check_EmailStr, DateTimeForStr,
                     RandomStr)
from app.ReturnCode import ReturnCode
from app.Config import SERVER_GULAOBURL

def getlist(request):
    return 0,0,0