def test_output(capsys):
    import task
    captured = capsys.readouterr()
    for i in range(1, 6):
        assert str(i) in captured.out