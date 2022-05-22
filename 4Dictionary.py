characterA = {'strength': 12, 'dexterity': 10, 'constitution': 13, 'intelligence': 9, 'wisdom': 18, 'charisma': 14}

# print the dictionary
print(characterA)

# for loop
for key in characterA:
    print(key, ':', characterA[key])

# Test if "strength" exists in your dictionary.
if characterA.get('strength'):
    print('the strength is ', characterA['strength'])
else:
    print('strength isn not a character stat')





# Test if "speed" exists in your dictionary.
if characterA.get('speed'):
     print(characterA['speed'])
else:
    print('speed isn not a character stat')