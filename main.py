import socket
import re
import click



@click.command()
@click.option('--host', prompt="target host ip", default='127.0.0.1', help='input the host you want to scan ')
@click.option('--ports', prompt="target ports", default="22", help="input the port you want to scan")
def start_scan(host, ports):
    final_ports_dict = port_form(ports)
    del_repeat(final_ports_dict)
    for port in final_ports_dict:
        get_info(host, port)



# 创建sockey， 探测端口
def get_info(host, ports):
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((host, ports))
        # 设置超时
        tcp_socket.settimeout(3)
        result = tcp_socket.recv(1024)
        if result:
            print("[+] {}端口开放， 响应信息{}".format(ports, result))

    except Exception as e:
        print(e)


# 格式化端口
def port_dict(dict):
    pass


# formalize ports
def port_form(dict):
    result = []
    dict = dict.replace(" ", "")
    dict2 = dict.split(',')
    for i in dict2:
        if '-' in i:
            pattern = r"\b(\d+)-(\d+)\b"
            number = re.findall(pattern, i)
            if number[0][0] < number[0][1]:
                for a in range(int(number[0][0]), int(number[0][1]) + 1):
                    result.append(a)
            else:
                print("Wrong input")
        else:
            result.append(int(i))
    return result

    # clear the repeated port


def del_repeat(dict):
    dict[:] = list(set(dict))


def get_host():
    host = input("input ip")
    return host


if __name__ == "__main__":
    start_scan()
