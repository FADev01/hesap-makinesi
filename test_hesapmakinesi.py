from hesapmakinesi import toplama
def test_hesapmakinesi_3_param():
    assert toplama()== "Bu işlem şimdilik yapılamaz!"

def test_hesapmakinesi_2_param():
    assert toplama()== "Bu işlem yapılabilir 'num1+num2'"
    