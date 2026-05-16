# Last updated: 5/16/2026, 12:28:06 PM
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        tmp_list = [[start, 0]]
        ind_used = [False]*len(bank)

        while tmp_list:

            tmp = tmp_list.pop(0)
            query_gene, num_change = tmp[0], tmp[1]

            if query_gene == end:
                return num_change


            for i in range(len(bank)):

                if not ind_used[i] and self.num_difference(query_gene, bank[i]):
                    tmp_list.append([bank[i], num_change + 1])
                    ind_used[i] = True

        return -1
    
    def num_difference(self, mut0, mut1):
        count = 0
        for i in range(len(mut0)):
            if mut0[i] != mut1[i]:
                count += 1
        return count == 1