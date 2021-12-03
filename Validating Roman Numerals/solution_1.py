import re

s = "DXXVIIII"

s = "CDXXIIIDV"


n = 'VLD'
m = 'IXC'


regex_pattern = "^M?((?:([VLD])|([IXC]){,3})(?<![I]{4})(?<![X]{4})(?<![C]{4})(?<![V]{2})(?<![L]{2})(?<![D]{2})(?!([IXC])\1([VLD])\1))+(?!.M.*)$"

print(re.match(regex_pattern, s))
