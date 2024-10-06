#!/usr/bin/env python3
import argparse

from algorithm.vinaigrette import encrypt, decrypt
from attack.guess_key import guess_key


def file_io(input_file, output_file, fun, *args, **kwargs):
    with open(input_file) as file:
        input_content = file.read()
    result = fun(input_content, *args, **kwargs)
    with open(output_file, "w") as file:
        file.write(result)


def app():
    parser = argparse.ArgumentParser(description="encrypt, decrypt, or crack a file.")
    subparsers = parser.add_subparsers(dest='mode', required=True)

    encrypt_parser = subparsers.add_parser('encrypt')
    encrypt_parser.add_argument('input_path')
    encrypt_parser.add_argument('output_path')
    encrypt_parser.add_argument('key')

    decrypt_parser = subparsers.add_parser('decrypt')
    decrypt_parser.add_argument('input_path')
    decrypt_parser.add_argument('output_path')
    decrypt_parser.add_argument('key')

    crack_parser = subparsers.add_parser('crack')
    crack_parser.add_argument('input_path')
    crack_parser.add_argument('max_key_length', type=int)

    args = parser.parse_args()

    if args.mode == 'encrypt':
        file_io(args.input_path, args.output_path, encrypt, args.key)

    elif args.mode == 'decrypt':
        file_io(args.input_path, args.output_path, decrypt, args.key)

    elif args.mode == 'crack':
        with open(args.input_path) as file:
            key = guess_key(file.read(), args.max_key_length)
            print(key)
