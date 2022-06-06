def morse_to_english(path):
    global sentence
    morse_dict = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
         '--.': 'G',   '....': 'H',     '..': 'I',
      '.---': 'J',    '-.-': 'K',   '.-..': 'L',
        '--': 'M',     '-.': 'N',    '---': 'O',
      '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U',
      '...-': 'V',    '.--': 'W',   '-..-': 'X',
      '-.--': 'Y',   '--..': 'Z',  '-----': '0',
     '.----': '1',  '..---': '2',  '...--': '3',
     '....-': '4',  '.....': '5',  '-....': '6',
     '--...': '7',  '---..': '8',  '----.': '9'}
    try:
        f = open(path)
        r = f.read()
        sentence = ''
        words = r.split('/')
        let = []
        for i in words:
            i = i.split()
            let.append(i)
        for i in let:
            for j in i:
                sentence += morse_dict[j]
            sentence += ' '
        print(sentence)
        f.close()
    except IOError:
        print("There is no file named " + path)
    except KeyError:
        print("Error in Morse Code")
    letters = {}
    for i in sentence:
        if i in letters:
            letters[i] += 1
        elif i != ' ':
            letters[i] = 1
    values = letters.values()
    values = list(set(values))      # הפיכה לסט בכדי למחוק כפילויות
    values.sort(reverse=True)
    for i in values:
        string = ''
        for j in letters:
            if letters[j] == i:
                string += j
        print(f'{string} - {i}')


if __name__ == "__main__":
    morse_to_english('morse1.txt')
