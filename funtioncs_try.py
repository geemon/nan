#functions with  position and keyword arguments
def make_shirt(size, message):
    'this function will print a shirt size and display a message on the shirt'
    print(f'the size of the shirt :{size}')
    print(f"the message on the shirt is :{message}")
make_shirt(12, '>>fEAR_god<<')

#keyword arguments with functions
make_shirt(size='m', message='<<<fear_GOD>>>>>')