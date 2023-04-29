# PSET-7
'''
Write a script that asks the user for some input with the following prompt: `'Enter some text:'`.
Then use the `.replace()` method to convert the text entered by the user into [`leetspeak`](https://en.wikipedia.org/wiki/Leet).

| Character   | Substitute |
| :---------- |:-------:|
| A  | 4 |
| B  | I3|
| E  | 3 |
| I  | 1 |
| H| \#  |
|M | /\\/\\ |
|O|0|
|S|5|
|T|7|
|U|(_)|
'''
#  Solution

text = input ("Enter  Some text: ")
text = text.replace("A", "4")
text = text.replace("E", "3")
text = text.replace("I", "1")
text = text.replace("B", "I3")
text = text.replace("H", "\#")
text = text.replace("M", "/\\/\\")
text = text.replace("O", "0")
text = text.replace("S", "5")
text = text.replace("T", "7")
text = text.replace("U", "(_)")
print(f'Your text in "leetspeak" is:  {text}' )
