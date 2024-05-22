import sender_stant_request
import data


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name): #solo cambia el first_name con el firs_name de prueba
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos
    # del diccionario de origen
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name # Se cambia el valor del parámetro firstName
    return current_body # Se devuelve un nuevo diccionario con el valor firstName requerido

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stant_request.post_new_user(user_body)
    # Compreba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""
    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stant_request.get_users_table()
    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1


# Función de prueba NEGATIVA first_name = "123"
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stant_request.post_new_user(user_body)
    assert response.status_code == 400
    print(response.status_code)
    assert response.json()["code"] == 400
    #assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                        # "Los nombres solo pueden contener caracteres latinos,  "\
                                         #"los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


def negative_assert_no_first_name(user_body):
    response = sender_stant_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    #assert response.json()["message"] == "No se enviaron todos los parámetros necesarios"