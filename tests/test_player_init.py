def test_imports():
    try:
        import players
    except (ImportError, ModuleNotFoundError):
        raise
    except Exception:
        raise
