from simpleinterest import calculate_SI

def test_calculate_SI():
    assert calculate_SI(1000,4,2) == 80.0
def test_calculate_SI_zero():
    assert calculate_SI(0,3,1) == 0.0  
    