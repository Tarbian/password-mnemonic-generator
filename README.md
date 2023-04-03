# Password and Mnemonic Generator
This Python script generates random passwords and corresponding mnemonic phrases to help you remember them.

# Usage
To use this script, simply run `python pass.py` from the command line. The following arguments are available:

+ `-n` or `--num`: the number of passwords to generate. Default is 1.
+ `-l` or `--length`: the length of the passwords to generate. Default is 12.
+ `-a` or `--alphabet`: the alphabet to use, specified as a string containing any combination of the following letters:
  + `l` or letters: include uppercase and lowercase letters in the password alphabet.
  + `d` or digits: include digits in the password alphabet.
  + `s` or symbols: include special symbols in the password alphabet.

For example, to generate three passwords with a length of 16 characters and containing only letters and digits, run the following command:

   ```sh
   python pass.py -n 3 -l 16 -a l_d
   ```
You can use the following bash script to redirect its output to a file:

   ```sh
   python pass.py -n 3 -l 16 -a l_d > output.txt
   ```

You can use the following bash script to redirect only passwords to a file:

   ```sh
   python pass.py -n 3 -l 16 -a l_d | awk 'NR%2==1' > output.txt
   ```

# Requirements
This script requires Python 3 and the following modules:

+ secrets
+ string
+ argparse
# License
This script is released under the MIT License.
