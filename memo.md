# Step1

## アプローチ

* @以降の部分はそのままで良い.
* @より手前の部分を考える.
    * まずは最初に出現する+以降の部分を消す.
    * その後 . を取り除く
    * これを同時に行うこともできそう
* 前から順番に見ていく
    * 英語の小文字の場合は`result`配列に追加
    * .の場合はむし
    * +の場合はそこで走査を終了
* 後ろから順番に@が出てくるまで見ていく
    * @が出てきたら終了
    * この方法だと@が複数ある場合をエラーとして弾けない
    * 結局前から見たほうがいいかも
* +以降が冗長に長い場合でも無駄なく走査することができそう
* 英語の小文字以外が出てきた場合もエラーにできる
* domainネームが`.com`で終わってなかったらエラー
* `@.com`となっているものはエラー
* @が複数あるものもエラー
    * @が+の後にあるものもエラーとして弾くべき？？
* locanameは+から始まってはいけない
* 時間計算量
    * メールアドレスの長さ分結果の配列に格納: O(m)
    * 綺麗にしたメールアドレスを文字列として`join`で連結. O(m)?
    * それをsetに追加: O(1)
    * 与えられるメールアドレスの個数(=n)分上記操作を繰り返す
    * 最終結果はsetの長さなので, O(1)で取得
    * 合計で O(n * m)
* 空間計算量
    * 綺麗にしたメールアドレスを保存するのにO(n * m)
    * setに追加して保存するのにO(n * m)
    * 合計で O(n * m)


## Code1

```python
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
            
```

# Step2

## Code2

* 変更なし
    * step3で気づいたが, `+`以降にinvalid characterがあった場合もエラーを返すようにする
    * 実際のユーザーの使用を考えると, `+`を故意的に使っているがメアドを表したいみたいになっているはず

```python
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
            
```

# Step3

## Code3

```python
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

```
# Memo

## ユースケースの想定

今回はinvalidなメールアドレスは全てエラーで処理したが, ユースケースの想定をするべきではあった.
今回だとユニークなアドレスの数を数えたいので, invalidとなる文字列をあらかじめ規定しておいて, それを含めずに個数を数えるか, `numUniqueEmails`で`try-except`するか.
`getUniqueEmail`自体はメールアドレスが`invalid`でエラーを返すのは関数の役割的にあっていそうだが...

https://github.com/Yoshiki-Iwasa/Arai60/pull/13#discussion_r1649832719
> とりあえず、ユースケースの想定ですね。これ、そもそもなんでこんなものを作りたいんだと思いますか。
> たとえば、これ、マーケティングのメールを送りたいのか、ある集団のやりとりを整理したいのか。
> つまり、たとえば、誤った入力が一つ入ったときに、全体として、そこそこ動いて欲しいのか、異常だといって止まって欲しいのか。それは何をしたいのかとの兼ね合いになるでしょう。


https://github.com/plushn/SWE-Arai60/pull/14#discussion_r2051712557
> 「大量のメールアドレスの候補が与えられ、正しいメールアドレスを得たい」というコードだと推測されるので、以下のような構造にして@がないメールアドレスが与えられても止まらないようにしたいかなあと思いました。

https://github.com/syoshida20/leetcode/pull/20#discussion_r2079714768
> これ、たとえば、データサイエンス目的の研究で、バッチで統計処理をしているならば、むしろ落ちて欲しいんですよね。そういう意味で状況次第です。