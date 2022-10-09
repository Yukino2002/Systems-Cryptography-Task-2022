cipher_text = 'sgf boyycvamy ysvafm rz dvta mosohoyf cfaf rz biorzsfqs ozm uvxbifsfid ktizfaohif oy ytug r afbioufm oii sgf ysvafm boyycvamy crsg sgfra uvaafybvzmrze aviirze goygfy tyrze vzf vl sgf barxfy oy yfkfzsffz ozm sgf vsgfa oy vzffqbzrzfbityyfkfz dvt ygvtim hf ohif sv ouufyy sgf cfhyrsf rl dvt uoz efzfaosf sgf uvaafybvzmrze goyg'
alphabet = 'fgbqmytczkorlehpxdsuwnvai'

plain_text = ''

for c in cipher_text:
    if c == ' ':
        plain_text += ' '
    else:
        plain_text += alphabet[((alphabet.find(c) - 12) +
                                len(alphabet)) % len(alphabet)]

print(plain_text)
