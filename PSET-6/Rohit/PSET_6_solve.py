# PSET-6

'''
Write a script such that it replaces only the first occurence of a word.

## Example

Consider the paragraph:
 > "Although most people consider **piranha**s to be quite dangerous, they are, for the most part, entirely harmless. \
Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. When confronted with humans, piranhas’ first instinct is to flee, not attack. \
Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans."

Your script should replace the first occurence of 'piranha' with 'fish'.

 > 'Although most people consider **fish**s to be quite dangerous, they are, for the most part, entirely harmless. \
Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. When confronted with humans, piranhas’ first instinct is to flee, not attack. \
Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans.'
'''

#  Solution

para =  "Although most people consider **piranha**s to be quite dangerous, they are, for the most part, entirely harmless. \
Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. When confronted with humans, piranhas’ first instinct is to flee, not attack. \
Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans."

para_new =  para.replace("piranha" , "fish" , 1)

print(para_new)
