import requests
import unittest

class TestTrainersAPI(unittest.TestCase):
    url = "https://api.pokemonbattle.me:9104"  
    trainer_id = "2500"

    def test_get_trainers_response_code(self):
        response = requests.get(f"{self.url}/trainers")
        self.assertEqual(response.status_code, 200)

    def test_trainer_name_in_response(self):
        response = requests.get(f"{self.url}/trainers", params={"trainer_id": self.trainer_id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("trainer_name", data)
        self.assertEqual(data["trainer_name"], "Mike")  

if __name__ == "__main__":
    unittest.main()
