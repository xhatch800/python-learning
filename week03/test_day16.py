"""Tests for Day 16 — Key Standard Library Modules (Part 1)"""
from day16_practice import *
from pathlib import Path


def test_os_sys_demo():
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Home Directory:  {os.environ.get('HOME')}")
    print(f"Custom Variable:  {os.environ.get('MY_VAR', 'My Var Not Present')}")
    print(f"/tmp Exists?  {os.path.exists('/tmp')}")
    print(f"List Directory:  {os.listdir('.')}")

    print(f"CLI Arguments:  {sys.argv}")
    print(f"Python Version:  {sys.version}")
    print(f"Python Lib Paths:  {sys.path}")


def test_get_env():
    assert get_env("MY_VAR") is None
    assert get_env("MY_VAR", "MY_DEFAULT") == "MY_DEFAULT"
    assert get_env("HOME", "No Home") != "No Home"


def test_script_info():
    result = script_info()
    assert re.match(r"\d+\.\d+\.\d+", result.get("python_version"))
    assert (args := result.get("argv")) and (len(args) > 0)


def test_json_demo():
    # Serialize to JSON string — like ObjectMapper.writeValueAsString()
    assert json.dumps({"name": "Tony", "age": 30}) == '{"name": "Tony", "age": 30}'

    # Deserialize from JSON string — like ObjectMapper.readValue()
    assert json.loads('{"name": "Tony", "age": 30}') == {"name": "Tony", "age": 30}

    # Write to file — like writeValue(file, obj)
    path = Path("tmp/tmp.out.json")
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        json.dump({"name": "Tony", "age": 30}, f, indent=2)

    # Read from file — like readValue(file, Class)
    with open(path, "r") as f:
        data = json.load(f)
        assert data == {"name": "Tony", "age": 30}


def test_serialize_user():
    result = serialize_user("Tony", 53, ["Engineer", "Artist"])
    assert result == '{"name": "Tony", "age": 53, "tags": ["Engineer", "Artist"]}'


def test_parse_config():
    result = parse_config("""
    {
        "name" : "John",
        "age" : 44
    }
    """)

    assert result == {"name": "John", "age": 44}


def test_parse_config_err(capsys):
    result = parse_config("""
    {
        "name" : "John"
        "age" : 
    }
    """)

    assert result is None
    assert capsys.readouterr().out.startswith("Json Error")


def test_datetime_demo():
    from datetime import datetime, date, timedelta

    # Current moment — like LocalDateTime.now()
    now = datetime.now()
    print(f"Now = {now}")

    # Specific date — like LocalDate.of(2024, 1, 15)
    print(f"Specific date = {date(2024, 1, 15)}")

    # Format to string — like DateTimeFormatter
    print(f"Formatted date = {now.strftime('%Y-%m-%d %H:%M:%S')}")  # → "2024-01-15 09:30:00"

    # Parse from string — like LocalDateTime.parse()
    print(f"Parsed from string = {datetime.strptime('2024-01-15', '%Y-%m-%d')}")

    # Arithmetic — like .plus() / .minus()
    print(f"Tomorrow = {now + timedelta(days=1)}")
    print(f"Two Hours Ago = {now - timedelta(hours=2)}")

    # Access components
    print(f"Year = {now.year}, Month = {now.month}, Day = {now.day}, Hour = {now.hour}, Minute = {now.minute}")


def test_format_date():
    dt = datetime(year=2016, month=3, day=26, hour=13, minute=2, second=44)
    assert format_date(dt, "%Y-%m-%dT%H:%M:%S") == "2016-03-26T13:02:44"


def test_days_until():
    now = datetime(year=2017, month=3, day=26, hour=13, minute=2, second=44)
    dt = datetime(year=2016, month=3, day=26, hour=13, minute=2, second=44)
    assert days_until(dt, now) == -365


def test_re_demo():
    import re

    # Search anywhere in string — like Matcher.find()
    assert re.search(r"\d+", "order 42")  # → Match object (truthy), or None
    assert not re.search(r"\d+", "no digits")  # → None (falsy)

    # Match from the START of string only — like Matcher.matches() (anchored)
    assert re.match(r"\d+", "42abc")  # → Match object
    assert not re.match(r"\d+", "abc42")  # → None — doesn't start with digits

    # Find ALL non-overlapping matches — returns a list of strings
    assert re.findall(r"\d+", "a1 b22 c333") == ["1", "22", "333"]

    # Replace — like String.replaceAll() in Java
    assert re.sub(r"\s+", "-", "hello world") == "hello-world"

    # Match objects...
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "date: 2024-01-15")
    assert m.group(0) == "2024-01-15"  # full match → "2024-01-15"
    assert m.group(1) == "2024"  # first capture group → "2024"
    assert m.group(2) == "01"  # second → "01"

    # Compiling for reuse:
    pattern = re.compile(r"\d+")
    assert pattern.findall("a1 b22") == ["1", "22"]  # reuse without recompiling


def test_extract_email():
    assert (extract_emails("My emails are abc-info@tony.com and amateur_babe@gmail.com") ==
            ["abc-info@tony.com", "amateur_babe@gmail.com"])
    assert not extract_emails("No emails here")


def test_mask_phone():
    assert mask_phone("Call me at 614-990-2334 please") == "Call me at ***-***-2334 please"
    assert mask_phone("Call me at 614 990 2334") == "Call me at ***-***-2334"
    assert mask_phone("Call me at 6149902334") == "Call me at ***-***-2334"
    assert mask_phone("Call me at 614 990-2334") == "Call me at ***-***-2334"
    assert mask_phone("Call me at 614-9902334") == "Call me at ***-***-2334"
    assert mask_phone("Call me at 614-990-233") is None
