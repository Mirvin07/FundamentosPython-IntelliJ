def test_output(capsys):
    import task
    captured = capsys.readouterr()
    assert 'nombre' in captured.out and 'edad' in captured.out and 'curso' in captured.out