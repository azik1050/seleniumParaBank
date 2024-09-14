import pytest
from api.helpers.pet import Pet
from configs import BASE_URL
from api.data.pet_data import data


@pytest.mark.parametrize(
    ('pet_id', 'pet_name', 'pet_status'), data
)
def test_correct_pet_adding(pet_id, pet_name, pet_status):
    pet = Pet(
        base_url=BASE_URL,
        pet_id=pet_id,
        pet_name=pet_name,
        pet_status=pet_status
    )
    response = pet.add_pet()
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() == pet.pet_json, 'Wrong body'


@pytest.mark.parametrize(
    ('pet_id', 'pet_name', 'pet_status'), data
)
def test_pet_find(pet_id, pet_name, pet_status):
    pet = Pet(
        base_url=BASE_URL,
        pet_id=pet_id,
        pet_name=pet_name,
        pet_status=pet_status
    )
    pet.add_pet()

    response = pet.find_pet()
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() == pet.pet_json, 'Wrong body'