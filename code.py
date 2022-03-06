# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 00:51:39 2022

@author: phiba
"""
####576k words dict to list #####
# import json
# with open("words_dictionary.json") as json_file:
#     data=json.load(json_file)
# wordle_list=list()
# for key in data:
#     if len(key)==5:
#         wordle_list.append(key)


###3k most common words to list#### 
###source: ef.com

ef_3k_v1=list()
ef_3k_v2=list() 
with open("3k_words.txt","r") as a_file:
    for line in a_file:
        ef_3k_v1.append(line.rstrip("\n")) ## remove"\n" string


##correct length
for word in ef_3k_v1:
    if len(word)==5:
        ef_3k_v2.append(word)







### read in oxford 3000 and oxford 5000### 
###source: oxfordlearnersdictionaries.com
ox_v1=list()
ox_v2=list() 
### oxford words ###
with open("oxford_3000_and_5000.txt","r") as a_file:
    for line in a_file:
        ox_v1.append(line.rstrip("\n"))

##cleaning and correct length 
ox_v1=[i.split()[0] for i in ox_v1] ## only first word
for item in ox_v1:
    print(item)
    if item !='Â©' and len(item)==5:
        ox_v2.append(item)



### merge ef.com words with oxford words
final_words=list(set(ef_3k_v2+ox_v2))
        
final_words.append("crane") #important word which is somehow missing
#print(ef_3k_v2,"\n",final_words)










##function which randomly picks the secret word
def set_keyword(list):
    import random
    random.seed()
    return list[random.randint(0, len(list)-1)]

##the word user searches for##
keyword=str(set_keyword(final_words)) 
##the word user searches for##      







print(keyword)
output="_____"
### user interaction from now on 
print("write a word with 5 letters")
while "_" in output:
    user_input=str(input("write : "))
    if user_input.isalpha()==True and len(user_input)==5 and user_input in final_words:
        z=0
        for keychar in keyword:
            for char in user_input:
                #print(keychar,char,z)# visualize algorithm
                if keychar==char:
                    output=output[:z]+char+output[z+1:]
                    break
            z+=1
        print(output)
    else:
        print("\nWord not accepted!")

print("congratiolation!!!! searchword:",keyword)
            
        
     