import re
s = "aSJDhasd ajshdfg ayTDwq `12 131 427234 fAsdfa56d GDFASGDFAHSFDGq qq "
result = re.search(r"\d", s)
print(result)

import re
s = "Привет! Как дела? А у меня нормально."
result = re.findall(r"[цкнгшщзхждлрпвфчсмтбЦКНШЩЗХФВПРЛДЖЧСМТБ]\w+", s)
print(result)