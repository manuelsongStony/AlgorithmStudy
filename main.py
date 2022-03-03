# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=10
    a=[[0],[1]]*n
    print(a)
    a = [0]* n
    print(a)

    array= [i for i in range(20) if i%2 ==1]
    print(array)

    example_1=[1,2,3,4,5,5,5]
    remove_set={3,5}
    print([i for i in example_1 if i not in remove_set ])


    print([[0] * 3 for _ in range(4)])
    print("hi" ) for _ in range(4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
