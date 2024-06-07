import os
import sys

def load_banned_tables(config_file):
    with open(config_file, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_sql_files_for_banned_tables(banned_tables, directory='.'):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.sql'):
                with open(os.path.join(root, file), 'r') as sql_file:
                    sql_content = sql_file.read()
                    for table in banned_tables:
                        if table in sql_content:
                            return True, file, table
    return False, None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_banned_tables.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    banned_tables = load_banned_tables(config_file)
    
    found, file, table = check_sql_files_for_banned_tables(banned_tables)
    if found:
        print(f"Banned table '{table}' found in file: {file}")
        sys.exit(1)
    else:
        print("No banned tables found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
