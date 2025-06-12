def test_output(capsys):
    import task
    captured = capsys.readouterr()
    assert ('Eres mayor de edad' in captured.out or 'Eres menor de edad' in captured.out)