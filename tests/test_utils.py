from src import utils


def test_unpack_json():
    assert (utils.unpack_json()[0]['id']) == 441945886


def test_form_transaction():
    assert (utils.form_transaction(utils.unpack_json()[
                                       0])) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
    assert (utils.form_transaction(
        utils.unpack_json()[3])) == "23.03.2018 Открытие вклада\n -> Счет **2431\n48223.05 руб."


def test_form_address():
    assert (utils.form_address("Счет 41421565395219882431")) == "Счет **2431"
    assert (utils.form_address("MasterCard 7158300734726758")) == "MasterCard 7158 30** **** 6758"
