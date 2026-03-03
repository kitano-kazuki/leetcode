class Solution:
    def getUniqueEmail(self, email):

        def is_valid_letter(letter):
            non_english_valid = [".", "+", "@"]
            if letter in non_english_valid:
                return True
            if ord("a") <= ord(letter) and ord(letter) <= ord("z"):
                return True
            return False

        idx = 0
        
        local_name = []
        ignore_local_name = False
        while idx < len(email) and email[idx] != "@":
            if not is_valid_letter(email[idx]):
                raise ValueError("invalid email: email must consist of [.+@a-z]")
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
            local_name.append(email[idx])
            idx += 1
        
        if idx == len(email):
            raise ValueError("invalid email: email must contain '@'")
        if not local_name:
            raise ValueError("invalid email: no character before '@'")

        assert email[idx] == "@"
        idx += 1

        domain_name = []
        while idx < len(email):
            if not is_valid_letter(email[idx]):
                raise ValueError("invalid email: email must consist of [.+@a-z]")
            if email[idx] == "@":
                raise ValueError("invalid email: email must contain exactly one '@'")
            domain_name.append(email[idx])
            idx += 1
        
        if not domain_name:
            raise ValueError("invalid email: no character after '@'")
        if len(domain_name) < 4 or "".join(domain_name[-4:]) != ".com":
            raise ValueError("invalid email: email must end with '.com'")
        if len(domain_name[:-4]) == 0:
            raise ValueError("invalid email: no character before '.com'")
        
        unique_email = "".join(local_name + ["@"] + domain_name)
        return unique_email
            
            
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_set = set()
        for email in emails:
            unique_email = self.getUniqueEmail(email)
            unique_email_set.add(unique_email)
        return len(unique_email_set)

            
