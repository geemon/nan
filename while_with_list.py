
unconfirmed_users = ['ama', 'kofi', 'ben']
confirmed_users =[]
while unconfirmed_users:
    confirmed = unconfirmed_users.pop()
    print(f"Veryfing user {confirmed.title()}")
    confirmed_users.append(confirmed)
for verifed in confirmed_users:
    print(verifed.title())