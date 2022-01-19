import pprint

message = 'elias calixto salazar'
count= {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)
print(pprint.pformat(count))


