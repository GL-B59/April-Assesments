#PSET 6
paragraph = "Although most people consider piranhas to be quite dangerous, they are, for the most part, entirely harmless.\
Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants.\
When confronted with humans, piranhas’ first instinct is to flee, not attack. \
Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas.\
If the fish are well-fed, they won’t bite humans."
a = paragraph.find("piranha")
new_paragraph = paragraph[:a] +"Fish" + paragraph[a+len("piranha"):]
print(new_paragraph)
