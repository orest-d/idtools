#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Unit tests for idtools
"""
import pytest
from idtools import *

class TestBasic:
    texts=["testThisText","test_ThisText","TEST_THIS_TEXT","test-this,text"]
    cap="CAp_Text"

    def test_id_to_list(self):
        assert id_to_list("") == []
        assert id_to_list(self.texts[0]) == ["test","This","Text"]
        assert id_to_list(self.texts[1]) == ["test","This","Text"]
        assert id_to_list(self.texts[2]) == ["TEST","THIS","TEXT"]
        assert id_to_list(self.cap) == ["C","Ap","Text"]

    def test_upper_camel_case(self):
        for t in self.texts:
            assert upper_camel_case(t) == "TestThisText"
        assert upper_camel_case("") == ""
        assert upper_camel_case(self.cap) == "CApText"

    def test_lower_camel_case(self):
        for t in self.texts:
            assert lower_camel_case(t) == "testThisText"
        assert lower_camel_case("") == ""
        assert lower_camel_case(self.cap) == "cApText"

    def test_all_caps(self):
        for t in self.texts:
            assert all_caps(t) == "TEST_THIS_TEXT"
        assert all_caps("") == ""
        assert all_caps(self.cap) == "C_AP_TEXT"

    def test_all_caps_separated(self):
        for t in self.texts:
            assert all_caps(t, "::") == "TEST::THIS::TEXT"
        assert all_caps("", "::") == ""
        assert all_caps(self.cap, "::") == "C::AP::TEXT"

    def test_small_caps(self):
        for t in self.texts:
            assert small_caps(t) == "test_this_text"
        assert small_caps("") == ""
        assert small_caps(self.cap) == "c_ap_text"

    def test_small_caps_separated(self):
        for t in self.texts:
            assert small_caps(t, "::") == "test::this::text"
        assert small_caps("", "::") == ""
        assert small_caps(self.cap, "::") == "c::ap::text"

    def test_indent(self):
        assert indent("") == ""
        assert indent("a\n b\nc") == "  a\n   b\n  c"
        assert indent("a\n b\nc", 1) == "  a\n   b\n  c"
        assert indent("a\n b\nc\n") == "  a\n   b\n  c\n"
        assert indent("a\n b\nc\n", "***") == "***a\n*** b\n***c\n"

    def test_dedent(self):
        assert dedent("") == ""
        assert dedent(" a\n  b\n c") == "a\n b\nc"
        assert dedent(" a\n  b\n c\n\n") == "a\n b\nc\n\n"
        assert dedent("  a\n\tb\n  c\n\n", tab=4) == "a\n  b\nc\n\n"
        assert dedent("  a\n\tb\n  c\n\n", tab=2) == "a\nb\nc\n\n"
        assert dedent("  a\n\tb\n  c\n\n", tab=1) == " a\nb\n c\n\n"

    def test_escape(self):
        assert escape("") == ""
        assert escape("a\nb") == "a\\nb"
        assert escape("a\rb") == "a\\rb"
        assert escape("a\tb") == "a\\tb"
        assert escape("a\\b") == "a\\\\b"
        assert escape('a"b') == 'a\\"b'
        assert escape("a'b") == "a\\'b"
