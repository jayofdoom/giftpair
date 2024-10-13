#!/usr/bin/python
#
# Copyright 2024 Jason Faulkner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
#
import copy
import random

import click

def is_valid(gifter, giftee, chosen, bad_pairs):
    if chosen and chosen.get(giftee) == gifter:
        return False
    if gifter == giftee:
        return False
    if gifter in bad_pairs and bad_pairs[gifter] == giftee:
        return False

    return True


@click.command()
@click.option("--name", "-n", multiple=True)
@click.option("--badpairs", "-b", multiple=True)
def main(name,badpairs):
    chosen = dict()
    bad_pairs = dict()
    for pair in badpairs:
        pairlist = pair.split(',')
        bad_pairs[pairlist[0]] = pairlist[1]
        bad_pairs[pairlist[1]] = pairlist[0]
    gifters = list(copy.deepcopy(name))
    giftees = list(copy.deepcopy(name))
    while gifters:
        gifter = random.choices(gifters)[0]
        giftee = random.choices(giftees)[0]
        if not is_valid(gifter, giftee, chosen, bad_pairs):
            if len(gifters) == 1:
                click.echo(f"Using invalid pair {gifter} buys for {giftee}.")
            else:
                continue
        gifters.remove(gifter)
        giftees.remove(giftee)
        chosen[gifter] = giftee
    for gifter,giftee in chosen.items():
        click.echo(f"{gifter} buys for {giftee}")
    if len(gifters) > 0 or len(giftees) > 0:
        click.echo(f"Leftover gifters: {gifters}, giftees: {giftees}")

if __name__ == "__main__":
    main()
