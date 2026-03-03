from typing import List


class Solution:
    def getUniqueEmail(self, email):
        idx = 0
        ignore_local_name = False

        local_name = []
        while idx < len(email) and email[idx] != "@":
            if ignore_local_name:
                idx += 1
                continue
            if email[idx] == "+":
                ignore_local_name = True
                idx += 1
                continue
            if email[idx] == ".":
                idx += 1
                continue
            if ord(email[idx]) < ord("a") or ord(email[idx]) > ord("z"):
                raise ValueError("email must be consist of +, ., @, or lowercase English letters.")
            local_name.append(email[idx])
            idx += 1
            continue

        if idx == len(email):
            raise ValueError("invalid email: use @ to specify domain name.")
        
        if not local_name:
            raise ValueError("invalid email: local name means empty.")

        assert email[idx] == "@"
        domain_name = []
        domain_name.append(email[idx])
        idx += 1
        while idx < len(email):
            if email[idx] == "@":
                raise ValueError("invalid email: multiple @ is found in the given email.")
            if email[idx] != "." and email[idx] != "+" and (ord(email[idx]) < ord("a") or ord(email[idx]) > ord("z")):
                raise ValueError("invalid email: email must be consist of +, ., @ or lowercase English letters.")
            domain_name.append(email[idx])
            idx += 1

        if "".join(domain_name[-4:]) != ".com":
            raise ValueError("invalid email: email must be end with .com")
        
        if len(domain_name[:-4]) == 0:
            raise ValueError("invalid email: empty string before .com suffix.")

        
        unique_email = "".join(local_name + domain_name)
        return unique_email
            
        
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_set = set()
        for email in emails:
            unique_email = self.getUniqueEmail(email)
            unique_email_set.add(unique_email)
        return len(unique_email_set)
            