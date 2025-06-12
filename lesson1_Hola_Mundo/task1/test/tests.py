def test_output(capsys):
    import task
    captured = capsys.readouterr()
    assert '¡Hola, mundo desde IntelliJ!' in captured.out