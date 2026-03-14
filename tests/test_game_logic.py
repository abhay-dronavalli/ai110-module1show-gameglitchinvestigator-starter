from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Bug 1: hint messages were swapped — guess > secret should be "Too Low", guess < secret should be "Too High"
def test_check_guess_hint_directions():
    outcome_high, _ = check_guess(70, 50)  # guess above secret → Too Low (go lower)
    assert outcome_high == "Too Low"

    outcome_low, _ = check_guess(30, 50)  # guess below secret → Too High (go higher)
    assert outcome_low == "Too High"


# Bug 2: get_range_for_difficulty returns the correct (low, high) for each difficulty
def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


# Bug 3: parse_guess returns ok=False and an error message for empty string or None
def test_parse_guess_invalid_input():
    ok, val, err = parse_guess("")
    assert ok is False
    assert err is not None

    ok, val, err = parse_guess(None)
    assert ok is False
    assert err is not None
