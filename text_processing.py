#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''punc_marks = ['.',',','"','{','}',';',':','=','!','@','#','$','%','^','&','*','(',')','+','?' , '/','|','~','//','😒']
inp_text = "Hello , world lets remove the punctuations marks ? shall we😒 "
final = ""
for i in inp_text:
    if i in punc_marks:
        continue 
    final = final + i
print(final)
'''


# In[7]:


punc_marks = ['.', ',', '"', '{', '}', ';', ':', '=', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '?', '/', '|', '~', '//', '😒']

def remve_punc(inp_text):
    final = ""
    for char in inp_text:
        if char in punc_marks:
            continue
        final += char
    return final


#inp_text = "Hello gg punch is removed ok! alr///😒 "
#output = remve_punc(inp_text)
#print(output)


# In[9]:


stop_words = ['a', 'the', 'of', 'below', 'above', 'with', 'for', 'underneath']

def remove_sw(inp_text):
    words = inp_text.split()
    final_words = []
    for word in words:
        if word not in stop_words:
            final_words.append(word)
    return ' '.join(final_words)


#inp_text = "hello i may be a below or above average guy with personality"
#output = remove_sw(inp_text)
#print(output)


# In[13]:


def split(text):
    words = text.split()
    for word in words:
        print(word)




# In[ ]:




