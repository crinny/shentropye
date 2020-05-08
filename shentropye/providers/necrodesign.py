import re
from typing import List

from shentropye.provider import Provider
from shentropye.regexp import valid_shentropye_code


class Necrodesign(Provider):
    def get_codes(self) -> List[str]:
        request = self.session.get("http://necrodesign.hldns.ru/c1a.php")
        code = request.html.find("center", first=True)

        if re.match(valid_shentropye_code, code.text):
            return [code.text]
        return []
