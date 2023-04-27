import configparser
from dataclasses import dataclass


@dataclass
class TgBot:
    """Класс для обращения к токену бота и id администратора"""
    token: str
    admin_id: int


@dataclass
class Config:
    """Класс, обобщающий настройки бота в один экземпляр"""
    tg_bot: TgBot


def load_config(path: str):
    """Функция для загрузки и чтения конфигурации из текстового файла

    :param path: путь к файлу
    :return:
    """
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config['bot']

    return Config(
        tg_bot=TgBot(
            token=tg_bot['token'],
            admin_id=int(tg_bot['admin_id'])
        )
    )


if __name__ == '__main__':
    config_ = load_config(r'D:\PycharmProjects\Pt9\bots\food_bot\config\bot_config.ini')
    print(config_.tg_bot.token)
    print(config_.tg_bot.admin_id)

