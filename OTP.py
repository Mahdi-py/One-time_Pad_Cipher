import random

def RandomKey(Text):
    '''
    :param Text: the text being translated
    :return: a random key after checking that it does not exist in keys file
    '''
    Asci = [random.randint(0,127) for i in Text]
    while IsThere(ToString(Asci)):
        Asci = [random.randint(0, 127) for i in Text]
    return ToString(Asci);


def Translate(Text, Key,Encryption):
    '''
    :param Text: The Text being translated
    :param Key: The used in the algorithm
    :param Encryption: boolean to indicate the process; if true: Encryption else: Decryption
    :return: The translated text. In case of duplicate Keys will return -1;
    '''

    if IsThere(Key=Key) and Encryption is True:
        return -1
    else:
        if Encryption is True:
            AddKey(Key=Key)
        Ascitxt=ToAsci(Text=Text)
        Ascikey=ToAsci(Key)
        TranslatedAsci = [i^j for i,j in zip(Ascitxt,Ascikey)]
        return ToString(TranslatedAsci)
def AddKey(Key):
    '''
    :param Key: The key being added to the keys file
    :return: nothing
    '''
    File = open("Keys.txt","a")
    #File.write(repr(Key)[1:len(Key)+1])
    print(File.name)
    File.write(str(ToAsci(Key)))
    File.write('\n')
    File.close()
def IsThere(Key):
    '''
    :param Key: The key you want to check if it does exist in the keys file
    :return: boolean value. True if the key exists, False if not
    '''
    Key=ToAsci(Key)
    File = open("Keys.txt","r")
    Lines= File.readlines()
    for l in Lines:
        if l.strip()==str(Key):
            return True
    return False

def ToAsci(Text):
    '''
    :param Text: the String being translated into asci code
    :return: array of asci codes
    '''
    Asci = [ord(i) for i in Text]
    return Asci
def ToString(Asci):
    '''
    :param Asci: Array of asci code
    :return: the string of the asci code
    '''
    str = ""
    for i in Asci:
        str = str+chr(i)
    return str
