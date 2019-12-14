from madlib import user_input

def test_one():
    expected = 'testing'
    actual = user_input('adj1', 'adj2', 'fn1', 'ptv1', 'fn2', 'adj3', 'adj4', 'pn1', 'la', 'sa', 'gn', 'adj5', 'pn2', 'adj6', 'pn3', 'n1', 'fn3', 'n2', 'pn4', 'n3', 'pn5')
    assert expected == actual