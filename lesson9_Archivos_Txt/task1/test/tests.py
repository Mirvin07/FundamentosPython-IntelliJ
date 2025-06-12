def test_file():
    with open('saludo.txt', 'r') as f:
        content = f.read()
        assert 'Hola desde Python' in content