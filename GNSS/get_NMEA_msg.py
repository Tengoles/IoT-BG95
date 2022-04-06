from pynmeagps import NMEAReader

def NMEA_message(GNSSPort):
    try:
        nme = NMEAReader(GNSSPort)
        (raw_data, parsed_data) = nme.read()
        return {"raw_data": raw_data, "parsed_data": parsed_data}

    except (nme.NMEAMessageError, nme.NMEATypeError, nme.NMEAParseError) as err:
        print(f"Something went wrong {err}")
        pass

def raw_data(GNSSPort):
    try:
        nme = NMEAReader(GNSSPort)
        (raw_data, parsed_data) = nme.read()
        return (raw_data)

    except (nme.NMEAMessageError, nme.NMEATypeError, nme.NMEAParseError) as err:
        print(f"Something went wrong {err}")
        pass

def parsed_data(GNSSPort):
    try:
        nme = NMEAReader(GNSSPort)
        (raw_data, parsed_data) = nme.read()
        return (parsed_data)

    except (nme.NMEAMessageError, nme.NMEATypeError, nme.NMEAParseError) as err:
        print(f"Something went wrong {err}")
        pass
