import unittest
from agent import review_retention


class RetentionTests(unittest.TestCase):
    def test_adverse_action_is_never_permitted(self):
        result = review_retention({"engagement_score": 20})
        self.assertIn("low-aggregate-engagement", result["issues"])
        self.assertFalse(result["adverse_action_permitted"])


if __name__ == "__main__":
    unittest.main()
