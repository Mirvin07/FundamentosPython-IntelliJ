def test_output(capsys):
    from task import saludar
    saludar()
    captured = capsys.readouterr()
    assert '¡Bienvenido al curso!' in captured.out