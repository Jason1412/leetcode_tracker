# Last updated: 5/16/2026, 12:26:42 PM
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        tmp = [word for word in words if word not in ban]
        return collections.Counter(tmp).most_common(1)[0][0]