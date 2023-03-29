def check_anagram(s,t):
    s_count={ }
    t_count={ }
    if len(s)!=len(t):
        return False
    else:
        for letter in s:
            if letter in s_count:
                s_count[letter]=s_count[letter] + 1
            else:
                s_count[letter]=1
        for lett_r in t:
            if lett_r in t_count:
                t_count[lett_r]=t_count[lett_r] + 1
            else:
                t_count[lett_r]=1
        return s_count ==t_count

reslt=check_anagram('anagram','nagaram')
print(reslt)

#check lenght of both strings
#if len same then find count of alphabets in both strings store in 2 dicts
#if keys and keyvalues same ,true