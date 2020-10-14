import argh
from sarcasm_formatter import sarcasm

def main():
	argh.dispatch_command(sarcasm)

if __name__ == '__main__':
	main()
