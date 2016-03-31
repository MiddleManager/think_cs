import testing

def vowel_in_string(str):
    vowels = "aeiouAEIOU"
    new_str = ""

    for i in str:
        if i not in vowels:
            new_str += i

    return new_str

def test_suite():
    testing.test(vowel_in_string("Compscience") == "Cmpscnc")
    testing.test(vowel_in_string("ABC") == "BC")
    testing.test(vowel_in_string("") == "")

test_suite()
