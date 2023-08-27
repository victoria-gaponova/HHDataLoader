from config import QUERIES_PATH


def sql_reading():
    sql_quries_dict = {}
    current_query_name = None
    current_query = ""
    with open(QUERIES_PATH, encoding='UTF-8') as fp:
        for line in fp:
            if line.startswith("--"):
                if current_query_name and current_query:
                    sql_quries_dict[current_query_name] = current_query
                current_query_name = line.lstrip("--").strip()
                current_query = ''
            else:
                current_query += line

    if current_query_name and current_query:
        sql_quries_dict[current_query_name] = current_query.strip()

    return sql_quries_dict