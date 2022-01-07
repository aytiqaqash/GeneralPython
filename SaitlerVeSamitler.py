def saitleri_tap(String):
    return [each for each in String if each in "aeiuoöüiıə"]

print(saitleri_tap("Ayti Qaqash"))

def samitleri_tap(String):
    return [each for each in String if each not in "aeiuoöüiıə"]

print(samitleri_tap("Ayti Qaqash"))