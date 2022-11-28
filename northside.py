ids = [
    "CK6RXK702473",
    "CKEL3Y539F40",
    "CKSLNX575302",
    "CKLRL46E752D",
    "CKLU6W7A9062",
    "CJUKFX4DE665",
    "CJYM3Z5933A9",
    "CJELN9575698",
    "CEKSJN6EF921",
    "CJULGB56285F",
    "CHJUPM7D0A85",
    "CJ8L8N52CCD0",
    "CH7QKT69B898",
    "CH7S937187B9",
    "CGBTHU774E52",
    "CGGTVR794038",
    "CFFHXQ4A40BA",
    "CGVU737472AA",
    "CGVSZ575091D",
    "CGBTFU773703",
    "CFESE572461E",
    "CG5LQC57A52F",
    "CG3STC743616",
    "CELSCL71D329",
    "CECL4A54B567",
    "CF8TLU744AB5",
    "CELSAL71C176",
    "CEYHNY49571C",
    "CF7U3X7A279A",
    "CDFSWF712F2C",
    "CDFSTZ70E510",
    "CDVR7B6C972C",
    "CEBMFQ5B1255",
    "CDGNC55F3B58",
    "CDGLN756F63A",
    "CB3N565CBC09",
    "CCDKX25110A4",
    "CBNQBQ688B5D",
    "CBFRC76D00C4",
    "CAVRVE6FD1D5",
    "CBQMZ65CE51A",
    "CC7JKU4D91CE",
    "CATLHU568C3C",
    "CAYTST788589",
    "CBMM2N59255F",
    "C9PQXN6B38DE",
    "CATLQ9570012",
    "C98S25703EEE",
    "CAMK374FDC49",
    "CAFJL34D4AEA",
    "C9QNVH5C56E3",
    "C8KMGG5ADD8E",
    "C8TS7J71109F",
    "C8ULYA559DA9",
    "C89QU8696808",
    "CAZL4E54A2BB",
    "CB3NAP5D18CB",
    "CB4KQ55280C3",
    "CB4M4Y59641B",
    "CB4RLL6DD028",
    "CB7QPN69E8E4",
    "CB7R4A6C11C8",
    "CB8KK5523119",
    "CB8T757462A2",
    "CBEM66599537",
    "CBESYZ7328E8",
    "CBGN825B5314",
    "CBGPUR665AA8",
    "CBGSKA72C6BE",
    "CBHKSC51D617",
    "CBGPPW5F52F8",
    "CBMND85EE60F",
    "CBMQ2Z66F548",
    "CBULEK56366C",
    "CBUMUC5CD071",
    "CBUR466C209C",
    "CBVKLN526964",
    "CBVL4M54C1ED",
    "CBVLC255D718",
    "CBVSUZ7453AA",
    "CBWRGZ6DEF39",
    "CBXLR957B6B0",
    "CBXQ9G67C522",
    "CBXS6D70C194",
    "CBXSJS728622",
    "CCAMM55BDB3C",
    "CCCRU26ECE0C",
    "CCCS2H6FA05C",
    "CCCSUQ741F59",
    "CCDRCY6D4128",
    "CCDRPP6EF2B3",
    "CCDSD571F81E",
    "CCDSNA72A272",
    "CCEMFJ5B0625",
    "CCERDS6BDED7",
    "CCQQYW6BA6EB"
]

committee = "A4EP6J588C05"

import httpx
import time
from socket import *



for meeting_id in ids:
    print(meeting_id)
    try:
        response = httpx.post(
            "https://go.boarddocs.com/tx/nisd/Board.nsf/PRINT-AgendaDetailed?open",
            data={"id": meeting_id, "current_committee_id": committee}
        )
    except timeout:
        continue
    except ConnectionResetError:
        continue
    open("NorthsideISD/" + meeting_id + "-agenda.html", "w").write(response.text)
    time.sleep(1)