# VINAIGRETTE

A program for encryption, decryption and cracking keys for the Vigenère cipher.


### Installation

- install: `pip3 install .`
- uninstall: `pip3 uninstall vinaigrette`

### Usage

- encryption: `vinaigrette encrypt <input_file_path> <output_file_path> <key>`
- decryption: `vinaigrette decrypt <input_file_path> <output_file_path> <key>`
- cracking:   `vinaigrette crack <input_file_path> <max_key_length>`


### Notes
- Files are assumed to only contain lowercase letters.
- The time to crack the key is directly proportional to the`<max_key_length>` you have provided.
