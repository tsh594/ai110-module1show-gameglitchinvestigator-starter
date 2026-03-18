from logic_utils import check_guess, parse_guess

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_negative_guess():
    outcome, _ = check_guess(-1, 50)
    assert outcome == "Too Low"

def test_decimal_input_rounds_down():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_non_number_input():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None

def test_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False

def test_exact_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_exact_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

# Out-of-range guesses (above max or below min) still get correct high/low feedback
def test_guess_above_range():
    outcome, _ = check_guess(200, 100)
    assert outcome == "Too High"

def test_guess_below_range():
    outcome, _ = check_guess(0, 1)
    assert outcome == "Too Low"

# parse_guess edge cases
def test_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_whitespace_input():
    ok, value, err = parse_guess("  ")
    assert ok is False

def test_decimal_rounds_toward_zero():
    ok, value, _ = parse_guess("99.99")
    assert ok is True
    assert value == 99

def test_negative_decimal_input():
    ok, value, _ = parse_guess("-3.7")
    assert ok is True
    assert value == -3

def test_large_number_input():
    ok, value, _ = parse_guess("99999")
    assert ok is True
    assert value == 99999

# Hint message direction checks
def test_too_high_message_says_go_lower():
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message
