import os

def check(target: str):
    if target == 'taeyoung':
        print("Hi {}! Welcome to vanmeruso's Homepage!".format(target))
        return True
    else:
        return False
    
def test_check():
    assert check(str(os.environ["OWNER"])) == True