import math
import sys
import pandas as pd


def get_data_csv(file_name: str):
    try:
        df = pd.read_csv(file_name, header=None)
    except (
        FileNotFoundError,
        PermissionError,
        pd.errors.ParserError,
        pd.errors.EmptyDataError,
        UnicodeDecodeError,
    ) as e:
        print(f"Error reading {file_name}: {e}", file=sys.stderr)
        sys.exit(1)

    return df


def is_valid_float(value):
    return isinstance(value, (int, float)) and math.isfinite(value)


def save_data_csv(df: pd.DataFrame, file_name: str):
    try:
        df.to_csv(file_name, index=False)
    except (OSError, ValueError, TypeError, UnicodeEncodeError) as e:
        print(f"Error saving CSV: {type(e).__name__}: {e}")
