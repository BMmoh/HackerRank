import re


s = """
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
"""

m = re.findall("(?P<Hex>(?<=.[^{])#(?:[\dA-F]{6}|[\dA-F]{3})(?=\W[^{]))+", s, re.I)

print('\n'.join(m))
