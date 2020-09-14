"""
Story
You are a h4ck3r n00b: you "acquired" a bunch of password hashes, and you want to decypher them. Based on the length,
you already guessed that they must be SHA-1 hashes. You also know that these are weak passwords:
maximum 5 characters long and use only lowercase letters (a-z), no other characters.

Happy hacking!

Notes:

pre-generating the full hash table is not advised, due to the time-limit on the CW platform
there will be only a few tests for 5-letter words (hint: start from the beginning of the alphabet)
"""
import hashlib
import itertools

def password_cracker(hash):
    return _password_cracker(hash)

def _password_cracker(hash):
    while hash not in hashdict:
        password = next(passgen)
        password = "".join(password)
        hashdict[hashlib.sha1(password.encode()).hexdigest()] = password
    return hashdict[hash]

def password_gen():
    library = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1,6):
        gen = itertools.product(library,repeat=i)
        for password in gen:
            yield password

def password_cracker2(hash):
    for length in range(6):
        for candidate in map("".join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length)):
            if hashlib.sha1(candidate.encode()).hexdigest() == hash:
                return candidate

passgen = password_gen()
hashdict = {}