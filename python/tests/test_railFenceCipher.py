# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/rail-fence-cipher/canonical-data.json
# File last updated on 2023-07-19

import unittest

from codingexercises.railFenceCipher import (
    decode,
    encode,
)


class RailFenceCipherTest(unittest.TestCase):
    def test_encode_with_two_rails(self) -> None:
        self.assertMultiLineEqual(encode("XOXOXOXOXOXOXOXOXO", 2), "XXXXXXXXXOOOOOOOOO")

    def test_encode_with_three_rails(self) -> None:
        self.assertMultiLineEqual(
            encode("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN"
        )

    def test_encode_with_ending_in_the_middle(self) -> None:
        self.assertMultiLineEqual(encode("EXERCISES", 4), "ESXIEECSR")

    def test_decode_with_three_rails(self) -> None:
        self.assertMultiLineEqual(
            decode("TEITELHDVLSNHDTISEIIEA", 3), "THEDEVILISINTHEDETAILS"
        )

    def test_decode_with_five_rails(self) -> None:
        self.assertMultiLineEqual(decode("EIEXMSMESAORIWSCE", 5), "EXERCISMISAWESOME")

    def test_decode_with_six_rails(self) -> None:
        self.assertMultiLineEqual(
            decode("133714114238148966225439541018335470986172518171757571896261", 6),
            "112358132134558914423337761098715972584418167651094617711286",
        )