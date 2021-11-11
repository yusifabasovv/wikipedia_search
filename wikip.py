import wikipedia as wikipedia
import pandas as pd
import socket

print('Welcome to Wikipedia')
print(' ' * 10)
print('Press "e" to exit')
print(' ' * 10)
index = []
col = []
lang = input('Enter search language : eg - ru,tr,en,az etc : ')
print(' ' * 10)

while True:

    search = input("Enter search :")

    index.append(search)

    if search == 'e':
        break
    else:
        try:
            wikipedia.set_lang(lang)
            try:

                result = wikipedia.summary(search, sentences=int(input('Enter sentences to print :')))
                print(result)

            except ValueError:
                print('Invalid, please enter numeric')

            col.append(result)
            df = {'Search': index, 'Info': col}
            df = pd.DataFrame(df)
            df.to_csv('Wiki')


        except (IndexError, wikipedia.exceptions.PageError):
            print('No information for', search)

        except (socket.gaierror, socket.error, ConnectionError):
            print('Connection Error')
            df = pd.read_csv('wiki')
            if search in df.Search.values:

                print("Data on saved CSV file :", df.loc[search, "Info"])

            else:
                print("No info on CSV file")



