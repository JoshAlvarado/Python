def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
  
    wordsearchdic = {}
    replace = ['.',',','!']
    for word in keywords:
        i = 0 # set i back to 0 for the first thing in list
        doc_number = [] # clear list 
        for sentence in doc_list: #each invidual item in a list
            sentence = sentence.lower() #lower the everything so that capilization isnt a factor
            for value in replace: #clean data of punctuation
                sentence = sentence.replace(value, '') #remove punctuation 
            if word in sentence.split(): # if keyword in item add index to list.
                doc_number.append(i) # add index to list
            i += 1 # increase index
        wordsearchdic[word] = doc_number # set finished list to dictionary
    return wordsearchdic        # return dict
        
        
        
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
print(multi_word_search(doc_list,keywords))