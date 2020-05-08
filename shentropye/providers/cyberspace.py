import re
from typing import List

from shentropye.provider import Provider
from shentropye.regexp import valid_shentropye_code


class Cyberspace(Provider):
    def get_codes(self) -> List[str]:
        request = self.session.get("https://www.cyberspace.org/~yollotl/")
        codes = request.html.find("td", first=True)
        valid_codes = []

        for line in codes.text.splitlines():
            if re.match(valid_shentropye_code, line):
                valid_codes.append(line)

        return valid_codes
