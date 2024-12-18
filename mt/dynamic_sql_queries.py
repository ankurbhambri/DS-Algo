'''
Write a Python script that constructs a dynamic SQL query based on two input JSON structures: columns_json and conditions_json. The columns_json specifies the columns to select, and the conditions_json specifies the conditions for the WHERE clause. The function should return a SQL query string.
'''

def solution(columns_json, conditions_json):
    def selected_columns(columns_json):
        columns = columns_json["columns"]
        temp = 'SELECT '
        temp += ', '.join(columns)
        return temp + ' FROM table_name '

    def conditional_query(conditions_json):
        conditions = conditions_json.get("conditions", {})
        if not conditions:
            return ""

        context = 'WHERE '
        condition_list = [
            "{} {} '{}'".format(k, v['operator'], v['value'])
            for k, v in conditions.items()
        ]
        context += ' AND '.join(condition_list)
        return context

    select_clause = selected_columns(columns_json)
    where_clause = conditional_query(conditions_json)
    return select_clause + where_clause

columns_json = {
    "columns": ["name", "age", "email"]
}

conditions_json = {
    "conditions": {
        "age": {"operator": ">", "value": 21},
        "email": {"operator": "LIKE", "value": "%@example.com"}
    }
}


columns_json = {
    "columns": ["name", "age", "email"]
}

conditions_json = {
    "conditions": {
        "age": {"operator": ">", "value": 21},
        "email": {"operator": "LIKE", "value": "%@example.com"}
    }
}

print(solution(columns_json, conditions_json))
