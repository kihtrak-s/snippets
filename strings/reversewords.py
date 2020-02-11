#input:
#First line: an integer that represents the number of testcases
#Followed by as many test cases. Each test case is a sentence where words are separated by dot('.')

#Output:
#The sentences where the last word becomes the first and vice versa

def reversewords():
    no_of_testcases = int(input())
    for case in range(no_of_testcases):
        sentence = input()
        split_array = sentence.split('.')
        new_sentence = '.'.join(reversed(split_array))
        print(new_sentence)

if __name__ == '__main__':
    reversewords()

