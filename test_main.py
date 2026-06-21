"""Tests for KBC game main module."""

import pytest
from qns import questions


def test_questions_exist():
    """Test that questions are loaded."""
    assert questions is not None
    assert len(questions) > 0


def test_question_structure():
    """Test that each question has the required structure."""
    for q in questions:
        assert "question" in q
        assert "options" in q
        assert "answer" in q
        assert len(q["options"]) == 4
        assert 1 <= q["answer"] <= 4


def test_levels_configuration():
    """Test prize level configuration."""
    levels = (1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
              640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000,
              75000000)
    assert len(levels) == 18
    assert levels[0] == 1000
    assert levels[-1] == 75000000


def test_checkpoint_stages():
    """Test checkpoint stages configuration."""
    stages = (10000, 320000, 75000000)
    assert stages[0] == 10000
    assert stages[1] == 320000
    assert stages[2] == 75000000
