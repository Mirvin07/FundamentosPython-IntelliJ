def test_output(capsys):
    from task import cuadrado
    result = cuadrado(4)
    assert result == 16