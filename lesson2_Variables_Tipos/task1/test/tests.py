def test_output(capsys):
    import task
    captured = capsys.readouterr()
    assert 'Hola, mi nombre es' in captured.out