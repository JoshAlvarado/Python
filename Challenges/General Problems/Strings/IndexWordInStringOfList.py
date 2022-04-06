def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.
    
    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """

    i = 0
    doc_number = []
    for sent in doc_list:
        sent = sent.lower()
        replace = ['.',',','!']
        for value in replace:
            sent = sent.replace(value,'')
        if keyword in sent.split():
            doc_number.append(i)
        else:
            pass
        i += 1 
    return doc_number
        
doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

print(word_search(doc_list,'that'))