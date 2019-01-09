class MyList(object):
    def __init__(self):
        self.abc_list = list("abc")

def append_to_list(my_list,string):
    my_list.abc_list.append(string)

def main():
    class_list = MyList()
    the_string = "hello"
    append_to_list(class_list,the_string)
    print(class_list.abc_list)

main()
