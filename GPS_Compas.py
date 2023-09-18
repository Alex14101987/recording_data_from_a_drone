from pymavlink import mavutil
import time


# Подключение к устройству
# master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)
# master = mavutil.mavlink_connection('/dev/ttyUSB0', baud=57600)
master = mavutil.mavlink_connection('udp:127.0.0.1:14551', baud=115200)

# # Отправка запроса
# master.mav.command_long_send(
#     master.target_system, # ID системы, к которой отправляется запрос
#     master.target_component, # ID компонента, к которому отправляется запрос
#     mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, # Команда установки интервала сообщений
#     mavutil.mavlink.MAVLINK_MSG_ID_GPS_RAW_INT, # Первый параметр команды (тип сообщения)
#     100, # Второй параметр команды (интервал в микросекундах)
#     0, # Третий параметр команды (зарезервировано)
#     0, # Четвертый параметр команды (зарезервировано)
#     0, # Пятый параметр команды (зарезервировано)
#     0, # Шестой параметр команды (зарезервировано)
#     0, # Седьмой параметр команды (зарезервировано)
#     0
# )


# start_time = time.time()
# while True:
#     msg = master.recv_match()
#     # print(msg)
#     if msg:
#         try:
#             if msg.get_type() == 'VFR_HUD':
#                 heading = msg.heading
#             if msg.get_type() == 'GPS_RAW_INT':
#                 latitude = msg.lat / 10000000.0  # Перевод широты из 1e-7 градусов в градусы
#                 longitude = msg.lon / 10000000.0  # Перевод долготы из 1e-7 градусов в градусы
#                 altitude = msg.alt / 1000.0  # Перевод высоты из миллиметров в метры
#                 data = {
#                     'time': time.time() - start_time,  # Вычисляем время от начала выполнения скрипта
#                     'heading': heading,
#                     'latitude': latitude,
#                     'longitude': longitude,
#                     'altitude': altitude
#                 }
#                 print('\n', f"Time: {data['time']:.2f} seconds")
#                 print(f"Heading: {heading:.2f} degrees")
#                 print(f"Latitude: {latitude:.6f} degrees")
#                 print(f"Longitude: {longitude:.6f} degrees")
#                 print(f"Altitude: {altitude:.2f} meters", '\n')
#         except:
#             continue    
#     # time.sleep(0.5)
#     # else:
#     #     print('msg=None')
#     #     break
print(master)
msg = master.recv_match(blocking=True)

# msg = master.recv_match()
while True:
        
    try:
        print(master.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)
