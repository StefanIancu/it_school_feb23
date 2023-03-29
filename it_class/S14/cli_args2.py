import argparse


print("hello")

argparser = argparse.ArgumentParser()
argparser.add_argument("symbol", type=str)
argparser.add_argument("mul", type=int)
args = argparser.parse_args()
# sep -> separator 
#-v -> verbose = afiseaza mesajele hello si bye daca este setat la true

print(args.symbol * int(args.mul))

print("bye")