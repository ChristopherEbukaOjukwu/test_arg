import argparse

def add_numbers():
    parser = argparse.ArgumentParser(description='Add two numbers.')
    parser.add_argument('--num1', type=float, required=True, help='First number to add')
    parser.add_argument('--num2', type=float, required=True, help='Second number to add')
    
    args = parser.parse_args()
    
    result = args.num1 + args.num2
    print(f'The sum of {args.num1} and {args.num2} is: {result}')

if __name__ == '__main__':
    add_numbers()
