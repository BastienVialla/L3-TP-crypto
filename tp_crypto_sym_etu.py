# -*- coding: utf-8 -*-
# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate

import os
import random

CHARACTERS = 'abcdefghijklmnopqrstuvwxyz0123456789 '

####################################
# 1.1 Chiffrement de César
####################################

def get_char_idx(char: str) -> int:
    """
        Function that returns the index of char in the string CHARACTERS.

        Examples: get_char_id('a') == 0, get_char_id('t') == 19, get_char_id('5') == 31

        Asumptions: char is in CHARACTERS

        Inputs:
            - char: the character to check

        Ouputs:
            - The index of char in the string CHARACTERS.
    """
    assert char in CHARACTERS, f'{char} is not in CHARACTERS'
    
    return

def get_translation_table(string1: str, string2: str) -> dict:
    """
        Function that construct a dictionnary matching each ascii code of characters of string1 with the ascii code of the corresponding characters of string2.

        Examples: get_translation_table('abcd', 'etks') -> {97: 101, 98: 116, 99: 107, 100: 115}

        Hints: Looks at the str.maketrans() function in the python documentation

        Assumptions: string1 and string2 have the same length

        Inputs:
            - sring1: a string
            - sring2: a string
        
        Outputs:
            - A dictionnary
    """
    assert len(string1) == len(string2)

    return

def cesear_enc(plaintext: str, key: str) -> str:
    """
        Function that encrypt a plaintext with cesear cipher.

        Examples: cesear_enc('hello there', 'r') -> yv225q yv8v

        Hints:
            - In python you can concatenate string with + operator
            - Looks at string slices
        
        Assumptions:
            - key is in a single character
            - key is in CHARACTERS
            - all characters of plaintext are in CHARACTERS 

        Inputs:
            - plaintext: a string with the text to encrypt

            - key: a single character used as the key
        
        Outputs:
            - A string of the plaintext encrypted by ceasar cipher under the key.
    """
    assert len(key) == 1
    assert key in CHARACTERS
    for c in plaintext:
        assert c in CHARACTERS
    return 

def cesear_dec(ciphertext: str, key: str) -> str:
    """
        Function that decrypt a ciphertext encrypted with ceasear cipher.

        Examples: cesear_dec('yv225q yv8v', 'r') -> hello there

        Hints:
            - In python you can concatenate string with + operator
            - Looks at string slices
        
        Assumptions:
            - key is in a single character
            - key is in CHARACTERS
            - all characters of ciphertext are in CHARACTERS 

        Inputs:
            - plaintext: a string with the text to encrypt

            - key: a single character used as the key
        
        Outputs:
            - A string of the plaintext encrypted by ceasar cipher under the key.
    """
    assert len(key) == 1
    assert key in CHARACTERS
    for c in ciphertext:
        assert c in CHARACTERS

    return

##########################################
# 1.2 Cryptanalyse chiffrement de César
##########################################

def chars_occurences(string: str) -> dict:
    """
        The function count the occurences of each character of the string.

        Hints: Look at the get() method of dict object in python documentation

        Examples: char_occurences('aabc') -> {'a': 2, 'b':1, 'c': 1}
        
        Inputs:
            - string: a string 

        Outputs:
            - a dictionnary
    """

    return 

def chars_frequency(string: str) -> dict:
    """
        Function that computes for each characters of string the frequency at which the characters appears.

        Hints: 
            - Looks at the items() method of dict object in python documentation
            - A frequency is the number of occurence divided by the total length of the string

        Examples: chars_frequency('aabc') -> {'a': 0.5, 'b': 0.25, 'c': 0.25}

        Inputs:
            - string: a string 

        Outputs:
            - a dictionnary
    """

    return 

def guess_key(char1: str, char2: str) -> str:
    """
        Given two characters char1, char2 where char2 is the encryption of char1 the function return the key such that
        cesear_enc(char1, key) -> char2.
        
        Example: guess(' ', 's') -> t

        Assumptions: 
            - char1 and char2 are of length 1

        Inputs:
            - char1: a string of size 1
            - char2: a string of size 1
        
        Outputs:
            - a string of size 1
    """
    assert len(char1) == 1
    assert len(char2) == 1

    return 

def cesear_cryptanalysis(ciphertext: str) -> dict:
    """
        The function takes a ciphertext and return a decryption for each of the most frequent characters in french (' ', 'a', 'e').

        Exemples: cesear_cryptanalysis('nkrrufznkxk') -> {' ': 'c ggj5oc m ', 'a': 'dahhk6pdana', 'e': 'hello there'}

        Hints:
            - In a dictionnary, to find the key corresponding to the maximum value look at the "key" argument of python max function

        Assumptions: 
            - All characters of ciphertext are in CHARACTERS

        Inputs:
            - chipertext: a string of the ciphertext
        
        Outputs:
            - a dictionnary

    """
    for c in ciphertext:
        assert c in CHARACTERS

    return 

##########################################
# 2.1 Chiffrement de Vigenère
##########################################
MAX_KEY_SIZE = 15

def vigenere_enc(plaintext: str, key: str) -> str:
    """
        Function that encrypt the plaintext with vigenere cipher. The key size is limited to 15.

        Examples: vigenere_enc('hello there', 'jf') -> qjuqxe2mnwn

        Assumptions: 
            - size of the key is at least 1 and less than 15
            - every character of the plaintext is in CHARACTERS
            - every character of the key is in CHARACTERS

        Hints:
            - You can reuse cesear encryption function

        Inputs:
            - plaintext: a string to encrypt
            - key: a string 

        Outputs:
            - a ciphertext as a string
    """
    for c in plaintext:
        assert c in CHARACTERS, f'{c} is not a valid character'
    assert len(key) > 0 & len(key) <= MAX_KEY_SIZE
    for c in key:
        assert c in CHARACTERS

    return 

def vigenere_dec(ciphertext: str, key: str) -> str:
    """
        Function that decrypt the ciphertext encrypted with vigenere cipher under the key key.

        Examples: vigenere_dec('qjuqxe2mnwn', 'jf') -> hello there

        Assumptions: 
            - size of the key is at least 1 and less than 15
            - every character of the ciphertext is in CHARACTERS
            - every character of the key is in CHARACTERS

        Hints:
            - You can reuse cesear decryption function

        Inputs:
            - ciphertext: a string to decrypt
            - key: a string 

        Outputs:
            - a string
    """
    for c in ciphertext:
        assert c in CHARACTERS
    assert len(key) > 0 & len(key) <= MAX_KEY_SIZE
    for c in key:
        assert c in CHARACTERS

    return 

##########################################
# 2.2 Cryptanalyse chiffrement de Vigenère
##########################################

COINCIDENCE_INDEX_FR = 0.077

def coincidence_index(string: str) -> float:
    """
    The function compute the coincidence index of the string. 
    See https://fr.wikipedia.org/wiki/Indice_de_co%C3%AFncidence for a refresh of the definition.

    Examples: coincidence_index('hello there') -> 0.0909...

    Hints: 
        - You can reuse some previous functions

    Inputs: 
        - a string

    Outputs:
        - the coincidence index as a float
    """

    return 

def guess_key_size(ciphertext: str) -> int:
    """
        The function guess the size of the key used to encrypt the ciphertext.

        Hints:
            - you need to use the coincidence index
            - in python you can use string[i::j] to get the substring starting at i with a step of j characters

        Inputs:
            - ciphertext: a string

        Outputs:
            - the lenght of the key as an int
    """
    for c in ciphertext:
        assert c in CHARACTERS

    return 

def vigenere_guess_key(ciphertext: str) -> str:
    """
        The function guess the key used to encrypt the ciphertext. 

        Hints:
            - you get the key size with the previous function
            - you can use function from cesear cryptanalysis

        Inputs: 
            - ciphertext: a string

        Outputs:
            - the key as a string
    """
    return 

def vigenere_cryptanalysis(ciphertext: str) -> str:
    """
        Decypher a ciphertext encrypted with Vigenere cipher.

        Hints: 
            - you have both the decryption function and the guess key function

        Inputs:
            - ciphertext: a string 
        
        Outputs:
            - the decrypted text as a string
    """

    return 

#################################################
###
### Fonctions pré implémentées pour tester vos fonctions.
### Ces  fonctions sont appelées dans le programme principal.
### Il suffit donc de commenter/décommenter les lignes du programme principal
### pour exécuter ou non ces fonctions
###
#################################################

cesear_ciphertext = 'rwejyerwxeizwxqj3evznemfgnyfnjsyefze9euwn0jyeiwn0jef0fnjsyeytzotzwxefkknwrjef0jheqfeuqzxelwfsijeknjwyjevznqxejyfnjsyeufwkfnyjrjsyestwrfz2erjwhneutzwejz2eofrfnxevznhtsvzjesfzwfnyenrflnsjevznqxeuznxxjsyexjeywtz0jwenruqnvzjxeifsxevztnevzjehjextnyeijywfsljetzeijer3xyjwnjz2enqxesf0fnjsyeufxeijeyjruxefeujwiwjef0jheijxextwsjyyjxerweizwxqj3einwnljfnyeqfelwzssnslxezsjejsywjuwnxjevznekfgwnvzfnyeijxeujwhjzxjxehjyfnyezsemtrrjelwfsiejyerfxxnkevznesf0fnyeuwfynvzjrjsyeufxeijehtzerfnxeutxxjifnyejsewj0fshmjezsjertzxyfhmjeijegjqqjeyfnqqjerwxeizwxqj3evzfsyefejqqjejyfnyernshjejyegqtsijejyeinxutxfnyeizsehtzeijz2ektnxeuqzxeqtslevzjeqfert3jssjehjevzneqznejyfnyektwyezynqjeutzwejxuntssjwexjxe0tnxnsxejsewjlfwifsyeufweijxxzxeqjxehqtyzwjxeijxeofwinsxeqjxeizwxqj3ef0fnjsyezseujynyelfwhtseuwjstrrjeiziqj3ejyehjyfnyefeqjzwxe3jz2eqjeuqzxegjqejskfsyeizertsijeqjxeizwxqj3ef0fnjsyeytzyehjevznqxe0tzqfnjsyeqfexjzqjehmtxjensijxnwfgqjevznqxeutxxjifnjsyehjyfnyezsexjhwjyeitsyenqxehwfnlsfnjsyeuqzxevzjeytzyevztseqjeijhtz0wjezseotzwexneofrfnxevznhtsvzje0jsfnyefejsyjsiwjeufwqjweijxeutyyjwenqxejyfnjsyehts0fnshzxevznqxesjexjsewjrjyywfnjsyeufxerwxeutyyjwejyfnyeqfextjzweijerwxeizwxqj3erfnxeytzyjxeijz2esjexjyfnjsyeuqzxewj0zjxeijuznxeijxefssjjxejsekfnyerwxeizwxqj3ekfnxfnyehtrrjexnejqqjejyfnyeknqqjezsnvzjehfwexfextjzwejyextsegtsefewnjseijerfwnejyfnjsyefzxxnejqtnlsjxevzjeutxxngqjeijeytzyehjevznekfnxfnyezseizwxqj3eqjxeizwxqj3eywjrgqfnjsyeijutz0fsyjefeqfeujsxjjeijehjevzjeinwfnjsyeqjxe0tnxnsxexneufwerfqmjzweqjxeutyyjwexjertsywfnjsyeifsxeqjzwewzjenqxexf0fnjsyevzjeqjxeutyyjwejz2efzxxnef0fnjsyezseujynyelfwhtserfnxenqxesjeqf0fnjsyeofrfnxe0zextsej2nxyjshjehtsxynyzfnyezsjewfnxtsexzuuqjrjsyfnwjeijeyjsnweqjxeutyyjwefeinxyfshjenqesjyfnyeufxevzjxyntsevzjeqjeujynyeiziqj3exjerjyyjefekwjvzjsyjwezsejskfsyehtrrjehjqzneqf'
vigenere_ciphertext = '3vcjzu3vveje8woj4u7ylenvsmwfoz4xcf0ukdswofvxcix3bicf1vziqyfd5ymt0b9ddkl38qhegfvgcqgu6pxxf18eqikuwmhwzzquxnrcqiwfoz4xcugbwelyk7vrwet98qdz3u3iuhou6sxwfza1cog7rmvewezgrswevdqf0brmweo7rklsku7ylqyu6ylxyz4xcxku vrz1z8dlrv6zuxjyuueqxfaaslewevdfjfc5mwejz vdsmzqsxejzqq1xzz8mhz3uzpvetvbeljtdqtdxfyvdwjs 9ddevz8hujfvbifejz9dvtx8vxwjyu3vci0b9ph3fyzvllkvzxcqguxvxst34kve08vdhszbvtunyzquxnf0rfunwermwejz9dsjxxvyvjyutiwfodqyqen93qhembrrgekdqqdxy3wdtzou4eyfodqtufz37yhrk8 dsfyuuichueqqdnyu6svxkyrmwek8qvh0g8tlhe08vdpt0c efmkuuicgk62icyg32phesb9dgzxc2i1ewerrweguvpojfz elyf7zrfjfz dequ8uicjzuumvuucrmweje4dft0uuix2f05mvev6awcqu8xdtzku2ecruivrqjfxvdtzou2ylekdrmwel98xczz32icuue8dhxv35rqjxu9ive19zwlsyuvrcwk1rvgftdqtdwfyvwvzyu2ivei65xxwkcqhhxf4rvgntcqphxfyavvqkiqeyfoz4xcztu6iwnzuxeuhu8qtujt93qhejeuph3fz dfjzvzxcff6vyuxfivy0erzqtozyusioek8weqyfyadpttyvdojyuuyuxrzedd0g3vrwez9axchku7ylqyubsxqg3vrwervqwhzrzqgktyzqmqikczvdgrzquxnrcqtrxyzueljtdqghyg3 dxsfcvgujzuusqyf32wchxvzkqfoz4xcure9dtzku sxyfaasqerzqhhhuebvhe08qnrzxu9mcog7rmvewezgrswevdyjtvzxcffz4xhsjbvdsfx6vvcikcqtryzz8dlqyuvxdnk8 dfttfrmqh0cquxnrcqrheyz4dujsz xufoz4xcugcqquxf 5xwjxuvxdnzu2ecxuzavciku3vveje8woj4u3elxfd5ywjyuuix2f8vdvjzvziqyf 2yvexzbyhxfyvtxnyuuiveg84ihxfz4difodqquxfyavvqkiqjdnyvzxchu73icxouvpojfz elyf0zpojfe4mtzkuteueyvqwrj0bqiwey94detturdunk8qhhesv8mcjzvziqyfvawvnfz2slltz9dtzku6svxow2iciku sxyfxvdtzouwelxg3 dxsfyavvqkiqphxfyavvqkiqxujsw2eljtdqhhuuebeqykurdoff vrvjkuuichku7yhej38eljtdqphxff5mvntcqwlevv8dpfr2vyuerz9dstzdvvcxku3sqyxvziqyfyrrverzavcw0zqmoxfcrzdnk8 dtzku2ivev9 xhwfza1cf0c9mcf1vziqyfe4dsjz3 djfxx5rcrg39dlqyu4icqgfrmhszu0epfocqzxey94dh2oc iqhkutsqxz3 ydnzuarhexvzwrsfcatsqk7vrwfobvdgjfdvrlwf6vwcuud iueguumvyg8ticnru4iwfodqtdxfaaivyo94dtzku2icukdzxci0y2i1eyzqqhyzzqeckxz7yhszz8dxsfz4jdszutsprkutiozou2e'

def OK(b: bool, message: str = ''):
    return 'OK' if b else 'ERROR '+message

def test_get_char_idx():
    print('### Test get_char_idx ###')
    print(f'Check output type: '+OK(isinstance(get_char_idx('e'), int)))
    for idx, c in enumerate(CHARACTERS):
        print(f'Test {c}: '+OK(get_char_idx(c) == idx))
    print('\n')

def test_get_translation_table():
    print('### Test get_translation_table ###')
    print(f'Check output type: '+OK(isinstance(get_translation_table('abc', 'abc'), dict)))
    s1 = ''.join(random.sample(list(CHARACTERS), 15))
    s2 = ''.join(random.sample(list(CHARACTERS), 15))
    table = get_translation_table(s1, s2)
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        print(f'Test {i}: '+OK(table[ord(c1)] == ord(c2)))
    print('\n')

def test_cesear_enc():
    print('### Test cesear_enc ###')
    print(f'Check output type: '+OK(isinstance(cesear_enc('azer', 'k'), str)))
    print(f'Test 0: '+OK(cesear_enc('alice et bob', 'a') == 'alice et bob'))
    print(f'Test 1: '+OK(cesear_enc('pgm ', 'l') == '0rxk'))
    b = True
    for c in cesear_enc('alice et bob', 'e'):
        b = b and (c in CHARACTERS)
    print('Test 2: '+OK(b))
    print('\n')

def test_cesear_dec():
    print('### Test cesear_dec ###')
    print(f'Check output type: '+OK(isinstance(cesear_dec('azer', 'k'), str)))
    print(f'Test 0: '+OK(cesear_dec('alice et bob', 'a') == 'alice et bob'))
    print(f'Test 1: '+OK(cesear_dec('0rxk', 'l') == 'pgm '))
    b = True
    for c in cesear_enc('alice et bob', 'e'):
        b = b and (c in CHARACTERS)
    print('Test 2: '+OK(b))
    print('\n')

def test_chars_occurences():
    print('### Test chars_occurences ###')
    print(f'Check output type: '+OK(isinstance(chars_occurences(''), dict)))
    print('Test 0: '+OK(chars_occurences('jjj') == {'j': 3}))
    print('Test 1: '+OK(len(chars_occurences('jjjppoljb nz')) == len(set('jjjppoljb nz'))))
    b1 = True
    b2 = True
    b3 = True
    for k, v in chars_occurences(CHARACTERS+CHARACTERS).items():
        b1 = b1 and isinstance(k, str)
        b2 = b2 and isinstance(v, int)
        b3 = b3 and (v == 2)
    print('Test 2: '+OK(b1))
    print('Test 3: '+OK(b2))
    print('Test 4: '+OK(b3))
    print('Test 5: '+OK(len(chars_occurences('jjjppoljb nz')) == len(set('jjjppoljb nz'))))
    print('\n')

def test_chars_frequency():
    print('### Test chars_frequency ###')
    print(f'Check output type: '+OK(isinstance(chars_frequency(''), dict)))
    print('Test 0: '+OK(chars_frequency('jjj') == {'j': 1.0}))
    print('Test 1: '+OK(len(chars_frequency('jjjppoljb nz')) == len(set('jjjppoljb nz'))))
    b1 = True
    b2 = True
    b3 = True
    for k, v in chars_frequency(CHARACTERS+CHARACTERS).items():
        b1 = b1 and isinstance(k, str)
        b2 = b2 and isinstance(v, float)
        b3 = b3 and (v == 0.02702702702702703)
    print('Test 2: '+OK(b1))
    print('Test 3: '+OK(b2))
    print('Test 4: '+OK(b3))
    print('Test 5: '+OK(len(chars_frequency('jjjppoljb nz')) == len(set('jjjppoljb nz'))))
    print('\n')

def test_guess_key():
    print('### Test guess_key ###')
    print(f'Check output type: '+OK(isinstance(guess_key('a', 'a'), str)))
    print('Test 0: '+OK(len(guess_key('a', 'a')) == 1))
    print('Test 1: '+OK(guess_key('t', 't') == 'a'))
    print('test 2: '+OK(guess_key('m', 'b') == '0'))
    print('\n')

def test_cesear_cryptanalysis():
    print('### Test cesear_cryptanalysis ###')
    print(f'Check output type: '+OK(isinstance(cesear_cryptanalysis('lllskdmf'), dict)))
    print('Test 0: '+OK(len(cesear_cryptanalysis('lllskdmf')) == 3))
    print('Test 1: '+OK(' ' in cesear_cryptanalysis('ll')))
    print('Test 2: '+OK('e' in cesear_cryptanalysis('ll')))
    print('Test 3: '+OK('a' in cesear_cryptanalysis('ll')))
    print('Test 4: '+OK(cesear_cryptanalysis(cesear_ciphertext)[' '][:5] == 'mr et'))
    print('Test 5: '+OK(cesear_cryptanalysis(cesear_ciphertext)[' '][-5:] == 'ui la'))
    print('Test 6: '+OK(len(cesear_cryptanalysis(cesear_ciphertext)[' ']) == len(cesear_ciphertext)))
    print('\n')

def test_vigenere_enc():
    print('### Test vigenere_enc ###')
    print(f'Check output type: '+OK(isinstance(vigenere_enc('ool', 'k'), str)))
    print('Test 0: '+OK(vigenere_enc('alice et bob', 'a') == 'alice et bob'))
    print('Test 1: '+OK(vigenere_enc('alice et bob', 'nh') == 'nsvjrgr0mi1i'))
    b = True
    for c in vigenere_enc('alice et bob', 'edt'):
        b = b and (c in CHARACTERS)
    print('Test 2: '+OK(b))
    print('\n')

def test_vigenere_dec():
    print('### Test vigenere_dec ###')
    print(f'Check output type: '+OK(isinstance(vigenere_dec('qsdool', 'k'), str)))
    print('Test 0: '+OK(vigenere_dec('alice et bob', 'a') == 'alice et bob'))
    print('Test 1: '+OK(vigenere_dec('nsvjrgr0mi1i', 'nh') == 'alice et bob'))
    b = True
    for c in vigenere_dec('alice et bob', 'e'):
        b = b and (c in CHARACTERS)
    print('Test 2: '+OK(b))
    print('\n')

def test_coincidence_index():
    print('### Test coincidence_index ###')
    print(f'Check output type: '+OK(isinstance(coincidence_index('aaze'), float)))
    print('Test 0: '+OK(coincidence_index('') == 0.))
    print('Test 1: '+OK(coincidence_index('kklsmloiiifjrimkjdf') == 0.07602339181286549))
    print('Test 2: '+OK(coincidence_index(CHARACTERS+CHARACTERS) == 0.013698630136986313))
    print('\n')

def test_guess_key_size():
    print('### Test guess_key_size ###')
    print(f'Check output type: '+OK(isinstance(guess_key_size('eert'), int)))
    print('Test 0: '+OK(guess_key_size(vigenere_ciphertext[:100]) > 0))
    print('Test 1: '+OK(guess_key_size(vigenere_ciphertext[:100]) <= MAX_KEY_SIZE))
    print('Test 2: '+OK(guess_key_size(vigenere_ciphertext) == 6))
    print('\n')

def test_vigenere_guess_key():
    print('### Test vigenere_guess_key ###')
    print(f'Check output type: '+OK(isinstance(vigenere_guess_key(vigenere_ciphertext[:100]), str)))
    print('Test 0: '+OK(vigenere_guess_key(vigenere_ciphertext) == 'redfgv'))
    print('\n')

def test_vigenere_cryptanalysis():
    print('### Test vigenere_cryptanalysis ###')
    print(f'Check output type: '+OK(isinstance(vigenere_cryptanalysis(vigenere_ciphertext), str)))
    print('Test 0: '+OK(vigenere_cryptanalysis(vigenere_ciphertext)[:5] == 'mr et'))
    print('Test 1: '+OK(vigenere_cryptanalysis(vigenere_ciphertext)[-5:] == 'ui la'))
    print('Test 2: '+OK(len(vigenere_cryptanalysis(vigenere_ciphertext)) == len(vigenere_ciphertext)))
    print('\n')

if __name__ == '__main__':
    test_get_char_idx()
    #test_get_translation_table()
    #test_cesear_enc()
    #test_cesear_dec()
    #test_chars_occurences()
    #test_chars_frequency()
    #test_guess_key()
    #test_cesear_cryptanalysis()
    #test_vigenere_enc()
    #test_vigenere_dec()
    #test_coincidence_index()
    #test_guess_key_size()
    #test_vigenere_guess_key()
    #test_vigenere_cryptanalysis()