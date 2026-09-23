"""Regression tests for ADSAT-16: Validate division by zero handling in calculate_ratio.

All assertions are derived exclusively from the acceptance criteria stated in
Jira ticket ADSAT-16. No implementation details are assumed.
"""

import pytest

from calculator import calculate_ratio


# ---------------------------------------------------------------------------
# Scenario 1 — Positive: valid division returns correct ratio (ADSAT-16)
# ---------------------------------------------------------------------------

class TestCalculateRatioValidDivision:
    """calculate_ratio returns numerator / denominator for non-zero denominators."""

    def test_canonical_example_returns_five(self):
        """ADSAT-16: calculate_ratio(10, 2) must return 5."""
        result = calculate_ratio(10, 2)
        assert result == 5


# ---------------------------------------------------------------------------
# Scenario 2 — Positive (parametrised): additional valid inputs (ADSAT-16)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "numerator, denominator, expected",
    [
        (0, 5, 0),      # zero numerator
        (9, 3, 3),      # exact integer division
        (-10, 2, -5),   # negative numerator
        (10, -2, -5),   # negative denominator
    ],
    ids=[
        "zero_numerator",
        "exact_integer_division",
        "negative_numerator",
        "negative_denominator",
    ],
)
def test_calculate_ratio_valid_inputs(numerator, denominator, expected):
    """ADSAT-16: calculate_ratio returns numerator / denominator for valid inputs."""
    result = calculate_ratio(numerator, denominator)
    assert result == expected


# ---------------------------------------------------------------------------
# Scenario 3 — Negative: zero denominator raises ValueError (ADSAT-16)
# ---------------------------------------------------------------------------

class TestCalculateRatioDivisionByZero:
    """calculate_ratio must raise ValueError when the denominator is zero."""

    def test_zero_denominator_raises_value_error(self):
        """ADSAT-16: calculate_ratio(10, 0) must raise ValueError."""
        with pytest.raises(ValueError):
            calculate_ratio(10, 0)

    # -----------------------------------------------------------------------
    # Scenario 4 — Negative: error message explains denominator cannot be zero
    # -----------------------------------------------------------------------

    def test_zero_denominator_error_message_mentions_denominator_and_zero(self):
        """ADSAT-16: The ValueError message must explain the denominator cannot be zero."""
        with pytest.raises(ValueError) as exc_info:
            calculate_ratio(10, 0)
        message = str(exc_info.value).lower()
        assert "denominator" in message, (
            f"Expected 'denominator' in error message, got: {exc_info.value!r}"
        )
        assert "zero" in message, (
            f"Expected 'zero' in error message, got: {exc_info.value!r}"
        )

    # -----------------------------------------------------------------------
    # Scenario 5 — Edge: zero denominator with zero numerator still raises
    # -----------------------------------------------------------------------

    def test_zero_numerator_and_zero_denominator_raises_value_error(self):
        """ADSAT-16: The zero-denominator guard applies regardless of the numerator value."""
        with pytest.raises(ValueError):
            calculate_ratio(0, 0)
