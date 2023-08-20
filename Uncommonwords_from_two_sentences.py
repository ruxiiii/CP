class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        # set_s1 = set(s1.split())
        # set_s2 = set(s2.split())

        # combined = set_s1.union(set_s2)
        # uncommon_s1 = set_s1 - set_s2
        # uncommon_s2 = set_s2 - set_s1
        # common_words = {}

        # # for i in combined:
        # #     if i not in common_words:
        # #         common_words.add(i)


        # #for s1
        # for  i in set_s1:
        #     if i in common_words:
        #         common_words[i] +=1
        #     else:
        #         common_words[i] = 1

        # for  i in set_s2:
        #     if i in common_words:
        #         common_words[i] +=1
        #     else:
        #         common_words[i] = 1

        # result = list(uncommon_s1.union(uncommon_s2))

        # duplicates = [x for x,  count in common_words.items() if count==2 ]
        # result =  [word for word in result if word not in duplicates]
        # return result

        s1 = s1.split()
        s2 = s2.split()

        dic={}
        res = []

        for i in s1+s2:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] == 1:
                res.append(i)
        
        return res
