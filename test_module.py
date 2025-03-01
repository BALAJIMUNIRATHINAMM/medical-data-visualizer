import unittest
import medical_data_visualizer
import pandas as pd

class TestMedicalDataVisualizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = medical_data_visualizer.load_and_preprocess_data()

    def test_overweight_column(self):
        self.assertIn('overweight', self.df.columns)
        self.assertTrue(set(self.df['overweight'].unique()).issubset({0, 1}))

    def test_cholesterol_normalization(self):
        self.assertTrue(set(self.df['cholesterol'].unique()).issubset({0, 1}))

    def test_glucose_normalization(self):
        self.assertTrue(set(self.df['gluc'].unique()).issubset({0, 1}))

    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot(self.df)
        self.assertIsNotNone(fig)

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map(self.df)
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
