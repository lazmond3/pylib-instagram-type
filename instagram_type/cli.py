# -*- coding: utf-8 -*-
import hello
import hello.cli


def main():
    print(hello.core.get_hmm())

    print("----")
    hello.cli.hello()
    print("----")

if __name__ == "__main__":
    main()