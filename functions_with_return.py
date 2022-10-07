#a function with return value
def retur_value(firstname, surname):
    """returns a person full name"""
    full_name = f"{firstname} {surname}"
    return full_name.title()
artist = retur_value('lil', 'wayne')
print(artist)