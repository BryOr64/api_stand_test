import create_user_test
import data
import sender_stant_request


#prueba 1 positiva
def test_create_user_2_letter_in_first_name_get_success_response():
    create_user_test.positive_assert("Aa")


#prueba 2 positiva
def test_create_user_15_letter_in_first_name_get_success_response():
    create_user_test.positive_assert("Aaaaaaaaaaaaaaa")


#prueba 1 negativa
def test_create_user_1_letter_in_first_name_get_error_response():
    create_user_test.negative_assert_symbol("A")


#prueba 2 negativa
def test_create_user_16_letter_in_first_name_get_error_response():
    create_user_test.negative_assert_symbol("Aaaaaaaaaaaaaaaa")


#prueba 3 negativa
def test_create_user_has_space_in_first_name_get_error_response():
    create_user_test.negative_assert_symbol("A Aaa")


#prueba 4 negativa
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    create_user_test.negative_assert_symbol("\"№%@\",")

# Prueba 5. Usuario o usuaria creada con éxito. El parámetro firstName contiene caracteres latinos
def test_create_user_english_letter_in_first_name_get_success_response():
    create_user_test.positive_assert("QWErty")

#prueba 5 negativa
def test_create_user_has_number_in_first_name_get_error_response():
    create_user_test.negative_assert_symbol("123")


# Prueba 8 negativa
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    create_user_test.negative_assert_no_first_name(user_body)


# Prueba 9. Error
# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = create_user_test.get_user_body("")
    # Comprueba la respuesta
    create_user_test.negative_assert_no_first_name(user_body)


def test_create_user_number_type_first_name_get_error_response():
    user_body = create_user_test.get_user_body(12)
    #response = sender_stant_request.post_new_user(user_body)
    create_user_test.negative_assert_no_first_name(user_body)
    #assert response.status_code == 400