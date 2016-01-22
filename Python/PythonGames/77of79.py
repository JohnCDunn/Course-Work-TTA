#!/usr/bin/python3
# Simple program
import sys, random

def ur_future_hell(jobs: list) -> str:
    tuple(jobs)
    this_one = random.choice(jobs)
    return this_one

def main():
    jobs = []

    print('What professions do you like?')
    while len(jobs) < 3:
        # asking for a job
        jobs.append(input('>Job' + str(len(jobs)+1) + ': '))

    print('--------------------\nLooks like you\'re gonna become a <'\
        + ur_future_hell(jobs) + \
        '> in the future.')

if __name__ == '__main__':
    sys.exit(main())
