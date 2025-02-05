import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_example_1(client, courses_factory):
    # - проверка получения первого курса (retrieve-логика):
    # ARRANGE
    courses = courses_factory(_quantity=1)
    # ACT
    response = client.get('/api/v1/courses/')
    # ASSERT
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_example_2(client, courses_factory):
    # - проверка получения списка курсов (list-логика):
    # ARRANGE
    courses = courses_factory(_quantity=10)
    # ACT
    response = client.get('/api/v1/courses/')
    # ASSERT
    data = response.json()
    assert response.status_code == 200
    for i, course in enumerate(courses):
        assert data[i]['name'] == course.name


@pytest.mark.django_db
def test_example_3(client, courses_factory):
    # - проверка фильтрации списка курсов по `id`:
    # ARRANGE
    courses = courses_factory(_quantity=10)
    # ACT
    response = client.get(f'/api/v1/courses/?id={courses[3].id}')
    # ASSERT
    data = response.json()
    assert data[0]['name'] == courses[3].name
    assert response.status_code == 200

@pytest.mark.django_db
def test_example_4(client, courses_factory):
    # - проверка фильтрации списка курсов по названию:
    # ARRANGE
    courses = courses_factory(_quantity=10)
    # ACT
    response = client.get(f'/api/v1/courses/?name={courses[3].name}')
    # ASSERT
    data = response.json()
    assert data[0]['name'] == courses[3].name
    assert response.status_code == 200

@pytest.mark.django_db
def test_example_5(client, courses_factory):
    # - тест успешного создания курса:
    #   - здесь фабрика не нужна, готовим JSON-данные и создаём курс;
    # ARRANGE
    data = {'name': 'Test course'}
    # ACT
    response = client.post('/api/v1/courses/', data)
    # ASSERT
    assert response.data['name'] == data['name']
    assert response.status_code == 201

@pytest.mark.django_db
def test_example_6(client, courses_factory):
    # - тест успешного обновления курса:
    #   - сначала через фабрику создаём, потом обновляем JSON-данными;
    # Arrange
    courses = courses_factory(_quantity=1)
    data = {
        'name': 'name_for_test4'
    }
    # Act
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data)
    # Assert
    assert response.status_code == 200
    assert Course.objects.get(id=courses[0].id).name == data['name']
    assert response.data['name'] == data['name']

@pytest.mark.django_db
def test_example_7(client, courses_factory):
    # - тест успешного удаления курса.
    # ARRANGE
    courses = courses_factory(_quantity=1)

    # ACT
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    # ASSERT
    assert response.status_code == 204
    assert courses[0].id not in list(course.id for course in Course.objects.all())

