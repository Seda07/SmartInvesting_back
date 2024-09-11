import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_register_user():
    """
    Test the user registration endpoint.

    Given:
        - No user exists with the given username and email.

    When:
        - A POST request is made to the 'register' endpoint with valid user details.

    Then:
        - The response status code should be 201 Created.
        - The response should contain a 'tokens' field.
        - The 'tokens' field should contain both 'access' and 'refresh' tokens.
    """
    client = APIClient()
    url = reverse('register')  # Asegúrate de que el nombre de la vista coincida con tu configuración
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword123'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'tokens' in response.data
    assert 'access' in response.data['tokens']
    assert 'refresh' in response.data['tokens']


@pytest.mark.django_db
def test_login_user():
    """
    Test the user login endpoint with valid credentials.

    Given:
        - A user exists with the username 'testuser' and password 'testpassword123'.

    When:
        - A POST request is made to the 'login' endpoint with the correct username and password.

    Then:
        - The response status code should be 200 OK.
        - The response should contain a 'tokens' field.
        - The 'tokens' field should contain both 'access' and 'refresh' tokens.
    """
    client = APIClient()
    # Primero, crea un usuario para poder iniciar sesión
    url = reverse('register')  # Asegúrate de que el nombre de la vista coincida con tu configuración
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword123'
    }
    client.post(url, data, format='json')

    # Luego, inicia sesión
    url = reverse('login')  # Asegúrate de que el nombre de la vista coincida con tu configuración
    data = {
        'username': 'testuser',
        'password': 'testpassword123'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'tokens' in response.data
    assert 'access' in response.data['tokens']
    assert 'refresh' in response.data['tokens']


@pytest.mark.django_db
def test_login_user_invalid_credentials():
    """
    Test the user login endpoint with invalid credentials.

    Given:
        - No user exists with the username 'wronguser'.

    When:
        - A POST request is made to the 'login' endpoint with incorrect username and/or password.

    Then:
        - The response status code should be 401 Unauthorized.
        - The response should contain an 'error' field.
        - The 'error' field should indicate 'Invalid Credentials'.
    """
    client = APIClient()
    # Intenta iniciar sesión con credenciales inválidas
    url = reverse('login')  # Asegúrate de que el nombre de la vista coincida con tu configuración
    data = {
        'username': 'wronguser',
        'password': 'wrongpassword'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'error' in response.data
    assert response.data['error'] == 'Invalid Credentials'
