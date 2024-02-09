import requests
import configuration

def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)
#создать заказ с данными в теле запроса
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + str(track))
#получить сведения о заказе по его номеру