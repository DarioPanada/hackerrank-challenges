"""
Validating Email Addresses With a Filter

https://www.hackerrank.com/challenges/validate-list-of-email-address-with
-filter/problem
"""


def tokenize(e):
    # Handling
    tokens = e.split("@")

    if len(tokens) < 2:
        return tokens

    sub_tokens = tokens[1].split(".")

    return [tokens[0]] + sub_tokens


def valid_email(e):
    if len(e) != 3:
        return False

    conditions = [
        len(e[2]) <= 3,
        e[1].isalnum(),
        e[0].replace("-", "").replace("_", "").isalnum()
    ]

    return all(conditions)


def fun(email):
    email = tokenize(email)

    return valid_email(email)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    emails = ["it!%^#$@w3.com",
              "674&*($@djfj.in",
              "itsnothing"]

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
