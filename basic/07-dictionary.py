# deklarasi dictionary
dict = {'Name': 'Habibi', 'Age': '17', 'Job': 'Scientist'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# update dictionary
dict['Age'] = 20
dict['School'] = "SMKN 24"
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# delete dictionary
del dict['Name']  # menghapus key name
dict.clear()  # menghapus isi di dictionary
del dict  # menghapus dictionary
print("Dictionary Deleted :D")
