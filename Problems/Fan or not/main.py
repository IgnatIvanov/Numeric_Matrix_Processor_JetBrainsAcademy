def add_viewer(fan, fans=None):
    fan_name = fan.split()[0]
    if fans is None:
        return [fan_name]
    else:
        fans.append(fan_name)
        return fans