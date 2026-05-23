def format_linter_error(error: dict) -> dict:
    """Formatowanie pojedyńczych błędów"""
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """Sprawdzanie obecności błędów w projekcie"""
    return {
        "errors": [
            format_linter_error(error) for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    """Uporządkowana lista kodów-ostatateczna wersja"""
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
