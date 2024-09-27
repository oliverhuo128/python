# Import the argparse module
import argparse

# Create the parser object
parser = argparse.ArgumentParser(description='A module for string manipulation')

# Add the arguments to the parser
parser.add_argument("message", help="text to be manipulated", type=str)
parser.add_argument("--lower", help="convert text to lowercase", action="store_true")
parser.add_argument("--upper", help="convert text to uppercase", action="store_true")
parser.add_argument("--swapcase", help="swap the case of the text", action="store_true")
parser.add_argument("--find", help="find the given substring in the text", type=str)
parser.add_argument("--repeat", help="repeat the text a given number of times", type=int)

# Parse the arguments supplied through the command line
args = parser.parse_args()

# Print the arguments parsed by the parser object
print('Arguments:',vars(args))

# Process the text based on the arguments supplied
print('Original text:', args.message)
if args.lower:
    print('Text in lowercase:', args.message.lower())
if args.upper:
    print('Text in uppercase:', args.message.upper())
if args.swapcase:
    print('Text after swapping case:', args.message.swapcase())
if args.find is not None:
    if args.message.find(args.find) >= 0:
        print(f'The substring {args.find} was matched at position {args.message.find(args.find)}')
    else:
        print(f'The substring {args.find} was not found in the original text!')
if args.repeat is not None:
    print(f'The original text repeated {args.repeat} times is {args.message*args.repeat}')