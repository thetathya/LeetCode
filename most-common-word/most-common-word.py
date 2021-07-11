class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = paragraph.split()
        wc = {}
        for i in words:
            if i in banned:
                continue
            else:    
                if i not in wc:
                    wc[i] = 1
                else:
                    wc[i] += 1
        return max(wc, key=wc.get)