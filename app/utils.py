
import locale
from datetime import datetime

def get_russian_date():
    # Устанавливаем русскую локаль (для Windows может потребоваться "russian")
    try:
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, 'rus_RU') # вариант для Windows

    now = datetime.now()
    # %A - день недели, %d - число, %B - месяц, %Y - год
    return now.strftime('%A, %d %B %Y').lower()



