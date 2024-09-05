# **************************** Part 3 ***************************
"""
א.כתבופונקציההמקבלתתאריךלועזיבתורמחרוזתו2מספרים:הראשוןהואמספר
התאריכים המבוקש והשני הוא מספר הימים לדילוג, הפונקציה תחזיר רשימה של  התאריכים. יש להשתמש בפונקציות על."""

from datetime import datetime, timedelta

def get_dates(date: str, days: int, stride: int) -> list:
    date = datetime.strptime(date, '%d/%m/%Y')
    return [date + timedelta(days=i * stride) for i in range(days)]

print(get_dates('01/01/2021', 10, 2))