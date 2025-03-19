def get_number_of_words(content):

    # Counting words
    word_count = len(content.split())
    return word_count

def get_freq_of_xter(content):

    s = content
    freq = {}

    for c in s:
        x = c.lower()
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

   
    return freq
    
def get_sorted_dict(freq):


    def sort_on(dict):
        return dict["value"]

    #dict_ = []
    dict_arr = list(map(lambda x: {'key':x[0], 'value': x[1] }, freq.items()))
    #for key, value in freq.items():
     #   dict_.append({'key':key, 'value': value })

    dict_arr.sort(reverse=True, key=sort_on)

    return dict_arr
