import re

print(re.search(r"(the|a)", "One sentence. Another one? And the last one!").groups())