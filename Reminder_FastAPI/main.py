from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette import status
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.secret_key = str(uuid4())  # Секретный ключ сессии

# регистрация маршрута для статических файлов с префиксом /static
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

reminders = []


@app.post('/delete/{index}')  # Удаление напоминания
async def remove_reminder(index: int):
    reminders.pop(index)
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)  # status_code 303


@app.get('/', response_class=HTMLResponse)
@app.post('/', response_class=HTMLResponse)
async def home(request: Request):
    if request.method == 'POST':  # Если отправляем данные о напоминании
        form = await request.form()  # Данные из формы
        reminder_text = form['reminder']  # Текст напоминания из формы
        reminder_date = form['date']  # Дата напоминания из формы
        reminder_time = form['time']  # Время напоминания из формы
        date_str = f'{reminder_date} {reminder_time}'
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        reminders.append({'text': reminder_text, 'time': date_obj})
        return RedirectResponse(url='/',
                                status_code=status.HTTP_303_SEE_OTHER)  # Перенаправляем пользователя на домашнюю
        # страницу GET-запросом
    now = datetime.now()
    upcoming_reminders = []
    for index, reminder in enumerate(reminders):
        if reminder['time'] > now:  # Проверяем, чтобы время напоминания было будущим
            reminder['index'] = index  # Индекс напоминания для удаления
            upcoming_reminders.append(reminder)
    return templates.TemplateResponse('home.html', {'request': request,
                                                    'upcoming_reminders': upcoming_reminders})  # Отображаем шаблон


