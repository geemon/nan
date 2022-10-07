aliens=[]
for a_num in range(20):
    details={'color':'red', 'speed':'slow', 'points':5}
    aliens.append(details)
for alien in aliens[:3]:
    if alien['color']== 'red':
        alien['color']='brown'
        alien['speed']='medieum'
        alien['points']=10

        alien    
for alien in aliens[:5]:
    print(alien)        
