class employee():
    def __init__(self):
        print('employee created')


    def __del__(self):
        print("destroucter called")


def create_obj():
    print('making objects.....')
    obj=employee
    print('function end....')
    return obj

print('calling crate_obj()function.....')
obj=create_obj()
print('pragramm end....')