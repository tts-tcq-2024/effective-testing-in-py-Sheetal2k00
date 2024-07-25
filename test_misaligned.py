def format_color_map_entry(index, major, minor):
    return f"{index:02d} | {major:<9} | {minor:<9}"

def test_format_color_map_entry():
    result_1 = format_color_map_entry(0, "White", "Blue")
    result_2 = format_color_map_entry(1, "Red", "Orange")
    result_3 = format_color_map_entry(24, "Violet", "Slate")

    expected_1 = "00 | White     | Blue     "
    expected_2 = "01 | Red       | Orange   "
    expected_3 = "24 | Violet    | Slate    "

    print(f"Result 1: '{result_1}' (length: {len(result_1)})")
    print(f"Expected: '{expected_1}' (length: {len(expected_1)})\n")

    print(f"Result 2: '{result_2}' (length: {len(result_2)})")
    print(f"Expected: '{expected_2}' (length: {len(expected_2)})\n")

    print(f"Result 3: '{result_3}' (length: {len(result_3)})")
    print(f"Expected: '{expected_3}' (length: {len(expected_3)})\n")

    # Assert statements
    assert result_1 == expected_1, f"Assertion failed: {result_1} != {expected_1}"
    assert result_2 == expected_2, f"Assertion failed: {result_2} != {expected_2}"
    assert result_3 == expected_3, f"Assertion failed: {result_3} != {expected_3}"

test_format_color_map_entry()
