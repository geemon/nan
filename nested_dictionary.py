users={
   'nana_1':{
    'age':5, 'location':'accra' } ,

    'mark':{
        'age':10, 'location':'tema'
    }
}
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    age =user_info['age']
    location =user_info['location']
    print(f"age: {age}")
    print(f"location: {location}")

