import requests


class Pet:
    def __init__(self, base_url, pet_id, pet_name, pet_status):
        self.base_url = base_url
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_status = pet_status
        self.pet_json = {
            'id': self.pet_id,
            'category': {
                'id': self.pet_id,
                'name': self.pet_name
            },
            'name': self.pet_name,
            'photoUrls': [
                "string"
            ],
            'tags': [
                {
                    'id': self.pet_id,
                    'name': self.pet_name
                }
            ],
            'status': self.pet_status
        }

    def add_pet(self):
        return requests.request(
            method='POST',
            url=f'{self.base_url}/pet',
            headers={
                'content-type': 'application/json'
            },
            json=self.pet_json
        )

    def find_pet(self):
        return requests.request(
            method='GET',
            url=f'{self.base_url}/pet/{self.pet_id}'
        )

    def remove_pet(self):
        pass