from dataclasses import dataclass
from typing import Optional

import toml
from interaction import UserInteraction
from analysis import Analyzer


@dataclass
class Config:
    is_test_mode: bool


def parse_config(path: str = './config') -> Optional[Config]:
    config = toml.load(path)

    try:
        is_test_mode = config['TEST_MODE']
    except KeyError:
        return None

    return Config(is_test_mode=is_test_mode)


def main():
    if (cfg := parse_config()) is None:
        print('Не удалось прочитать конфигурационный файл')
        return -1

    if cfg.is_test_mode:
        UserInteraction().start()
    else:
        Analyzer().start()


if __name__ == '__main__':
    main()
