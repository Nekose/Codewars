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
hashdict = {}
import hashlib
import itertools
def password_cracker(hash):

    while hash not in hashdict:
        for generator in password_gen():
            for password in generator:
                password = "".join(password)
                hashdict[hashlib.sha1(password.encode()).hexdigest()] = password
    return hashdict[hash]
def password_gen():
    library = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1,6):
        gen = itertools.product(library,repeat=i)
        yield gen

