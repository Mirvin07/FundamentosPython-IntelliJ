def test_structure():
    import task
    assert hasattr(task, 'agregar_contacto') and hasattr(task, 'mostrar_contactos')