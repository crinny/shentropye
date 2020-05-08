from abc import ABC, abstractmethod
from typing import List

from requests_html import HTMLSession


class Provider(ABC):
    def __init__(self):
        self.session = HTMLSession()

    @abstractmethod
    def get_codes(self) -> List[str]:
        pass
