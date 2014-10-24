import urllib2

URL = 'https://stepic.org/media/attachments/lessons/4/clump_finding_data.txt' 
CODE = {'A':0,'C':1,'G':2,'T':3}
KMERS = set()
KMERS_LIST = []


#*************************HASH ALGORITHM*************************#
def code_convert(text, k):
    code_r = {0:'A', 1:'C', 2:'G', 3:'T'}
    seq_r = ''

    while len(seq_r) < k:
        seq_r =  code_r[text % 4] + seq_r
        text  = text // 4
    return seq_r


def pattern_search_hash(seq, k, L, times):
    global KMERS
    pattern = [[] for _ in range(4**k)]
    kmer_mask = 4 ** (k - 1) - 1
    kmer_value = 0
    for i in range(k):
        kmer_value = (kmer_value << 2) + CODE[seq[i]]
    
    for i in range(k - 1, len(seq)):
        kmer_value = ((kmer_value & kmer_mask) << 2) +  CODE[seq[i]]
        pattern[kmer_value].append(i - k + 1)
#        pattern[reverse_constant - int(reading_frame[::-1])] += 1  ###Convert a string
        
#    max_rep = max(pattern)
    
    for idx in range(len(pattern)):
        if len(pattern[idx]) >= times:
            dummy = 0
            pos_list = pattern[idx]
            pos_list.insert(0, 0)
            pos_list.append(len(seq) - k - 1)
            for pos in range(1, len(pos_list) - times - 1):
                if pos_list[pos + times - 1] - pos_list[pos] <= L - k + 1 and \
                    pos_list[pos + times] - pos_list[pos - 1] > L - k + 1:
                    KMERS.add(code_convert(idx, k))
                    print code_convert(idx, k)
                    break
                    
