import unittest
#import emotion_detection
from EmotionDetector.emotion_detection import emotionDetector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotionDetector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotionDetector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotionDetector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = emotionDetector("I am so sad about this")
        #self.assertEqual(result['dominant_emotion'], 'sadness')
        assert result['dominant_emotion'] == 'sadness'

    def test_fear(self):
        result = emotionDetector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
