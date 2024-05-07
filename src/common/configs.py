import os
from pathlib import Path

from pydantic import BaseSettings


class Configs(BaseSettings):
    """
    전체에서 사용하는 Config정보를 일원화하여 관리하기 위한 class
    환경마다 다른 설정은 .env파일에 작성해서 불러옴
    전체환경에서 공통으로 사용하는 설정은 아래에 직접 작성함
    """

    ENV: str
    VERSION: str = "0.0.1"
    SRC_DIR_PATH: str = os.path.join(Path(__file__).parent.parent.absolute())  # src디렉토리의 절대경로
    LOGGER_CONFIG_PATH: str = os.path.join(SRC_DIR_PATH, "logger_config.yaml")  # logger의 설정파일 경로

    class Config:
        # .env파일 불러오기
        env_file = ".env"
        env_file_encoding = "utf-8"


configs = Configs()
