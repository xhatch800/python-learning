def power(base, exp=2):
    return base ** exp


def summarize(*items):
    formatted_result = []
    for i, item in enumerate(items):
        formatted = f"Item {i + 1} is {item}"
        print(formatted)
        formatted_result.append(formatted)
    return formatted_result


def build_query(table, **filters):
    query = f"SELECT * FROM {table}"
    for i, (k, v) in enumerate(filters.items()):
        if i == 0:
            prefix = "WHERE"
        else:
            prefix = "AND"
        query += f" {prefix} {k} = {v}"
    return query


print(f"Power 2^2 = {power(2, 2)}")

print(f"Power 4^3 with specific params = {power(base=4, exp=4)}")

print(f"Summarize : {summarize("a", "b", "c")}")

print(f"Build Query : {build_query("employees", employee_id="a3889898", dept="SALES")}")

print(f"Build Query no filters : {build_query("employees")}")
