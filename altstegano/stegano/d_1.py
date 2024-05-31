# Bartosz Majkowski

from len_maximum import LEN_MAXIMUM


def d_1():
    watermark = open('watermark.html').readlines()
    msg = ''
    for line in watermark:
        helper = line.replace('\n', '')
        if helper[-1] == ' ':
            msg += '1'
        else:
            msg += '0'
        if len(msg) == LEN_MAXIMUM:
            break
    h_msg = ''
    for i in range(0, len(msg), 4):
        h_number = hex(int(msg[i:i + 4], 2))[2:].upper()
        h_msg += h_number
    with open('detect.txt', 'w+') as f:
        f.write(h_msg.upper())

# def d_1():
#     watermark_html = open('watermark.html').readlines()
#     message = ''
#
#     for line in watermark_html:
#         stripped_line = line.replace('\n', '')
#         if stripped_line[-1] == ' ':
#             message += '1'
#         else:
#             message += '0'
#         if len(message) == 64:
#             break
#
#     hex_message = ''
#     for i in range(0, len(message), 4):
#         hex_digit = hex(int(message[i:i+4], 2))[2:].upper()
#         hex_message += hex_digit
#
#     with open('detect.txt', 'w') as f:
#         f.write(hex_message.upper())
