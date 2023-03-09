import string
import random
from tkinter import Button, Entry

class generador():

    def gen():
        small_alphabets=string.ascii_lowercase
        capital_alphabets=string.ascii_uppercase
        numbers=string.digits
        special_charecters=string.punctuation

        all = small_alphabets+capital_alphabets+numbers+special_charecters
        password_length=int(length_Box.get())   