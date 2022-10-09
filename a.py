text = 'sgf boyycvamy ysvafm rz dvta mosohoyf cfaf rz biorzsfqs ozm uvxbifsfid ktizfaohif oy ytug r afbioufm oii sgf ysvafm boyycvamy crsg sgfra uvaafybvzmrze aviirze goygfy tyrze vzf vl sgf barxfy oy yfkfzsffm ozm sgf vsgfa oy vzffzrzfbityyfkfz dvt ygvtim hf ohif sv ouufyy sgf cfhyrsf rl dvt uoz efzfaosf sgf uvaafybvzmrze goyg'
alphabet = 'fgbqmytczkorlehpxdsuwnvai'

def decrypt(text, alphabet):
    result = ''
    for c in text:
        if c == ' ':
            result += ' '
        else:
            result += alphabet[((alphabet.index(c) - 1 - 11) + 25) % 25]
    return result

print(decrypt(text, alphabet))