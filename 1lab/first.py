import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', nargs='?', default='Andrey')
parser.add_argument('-p', '--path')
parser.add_argument('-q', '--noQ', action="store_true")
args = parser.parse_args()
print(f"Hi {args.name}!")
print(args)

if os.path.exists(str(args.path)):
    if args.noQ:
        os.remove(args.path)
        exit(2)
    else:
        confirm = input(f'\n{args.name}, do you want to remove file? ')
        if confirm == "y" or confirm == "yes":
            os.remove(args.path)
            print("File has been deleted")
        else:
            print("File has not been deleted")
else:
    print("File doesnt exist")

