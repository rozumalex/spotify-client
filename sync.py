#!/usr/bin/env python

from utils import get_sync_args
import os


def main():
    for args in get_sync_args():
        command = " ".join(args)
        os.system(command)


if __name__ == "__main__":
    main()
