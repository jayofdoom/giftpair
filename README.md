# giftpair

This is a little script I made to help my mom with a family
white elephant.

Install:
    python -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Usage:
    python giftpair.py -n name1 -n name2 .. -n nameN
    name2 buys for name1
    name3 buys for name5

This will:
    - ensure everyone gets a gift from a random person
    - not the same random person
