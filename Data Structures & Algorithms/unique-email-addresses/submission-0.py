class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def preprocess(n):
            res=[]
            for c in n:
                if c==".":
                    continue
                if c=="+":
                    return "".join(res)
                res.append(c)
            return "".join(res)

        seen=set()

        for email in emails:
            local,domain=email.split('@')
            processed_local=preprocess(local)
            minimal_email=processed_local+'@'+domain
            if minimal_email not in seen:
                seen.add(minimal_email)
        return len(seen)