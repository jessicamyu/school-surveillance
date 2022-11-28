ids = [
    "CGJGTH455B8F",
    "CFVP6261AE6C",
    "CFVP6G61B9C4",
    "CFVP2R617B85",
    "CFVP38619D06",
    "CFVP2A617997",
    "CJ8LRK575421",
    "CJMPPB658F21",
    "CFVP9261D15C",
    "CJ8HKJ464C0A",
    "CFVNXC6154D9",
    "CFVNXX61680D",
    "CFVNM65F3C6A",
    "CFVNMP5F5894",
    "CE4GT545378E",
    "CE4GTK453B11",
    "CG4NEF5F917C",
    "CD2HKX48F07D",
    "CDFLJL56CDD3",
    "CEGPLB651ACF",
    "CEGPSU65D12C",
    "CC4S4J70C9BA",
    "CC4S6470E777",
    "CBJJKR4D8724",
    "CBJJLY4DC59F",
    "CBAMT25CB41B",
    "CADMAK5711DA",
    "CADMHK5724D6",
    "CADM6L56C659",
    "CADM9J56EC71",
    "CADLJB565C32",
    "C67KGZ50E259",
    "C67KRC50FA90",
    "C67KQS50ED0D",
    "C9QKZZ54090E",
    "C35GS8445613",
    "C67KE250CBB6",
    "C88NRZ609926",
    "C35GQH443258",
    "C35GQW4444BA",
    "C89R2M69FF76",
    "C35GM8441998",
    "C67KB250B89E",
    "C35GLR440C3D",
    "C7BNZY6197C1",
    "C35GL843F95C",
    "C35GH543D6BC",
    "C35GHL43E7F5",
    "C2FGLS439A7D",
    "C2FGMD43A3FD",
    "C5KLMB43FAC3",
    "C2FGFK437561",
    "C2FGLB438C87",
    "C3MGE54365F2",
    "BZSH9A4760DE",
    "BZSH8S474E0E",
    "BYSH3246763E",
    "BYSH474689C8",
    "BYJJRC4E6968",
    "BYJJT84E8A8C",
    "BY2QBC67BF3F",
    "BZ7HKB481927",
    "BYKV3J6E4690",
    "BX2TMB7800B4",
    "BX2TN7782407",
    "BYKV446E697B",
    "BYPTMN723ECC"
] 

committee = "A4EP6J588C05"

import httpx
import time
from socket import *



for meeting_id in ids:
    print(meeting_id)
    try:
        response = httpx.post(
            "https://go.boarddocs.com/fl/polk/Board.nsf/PRINT-AgendaDetailed?open",
            data={"id": meeting_id, "current_committee_id": committee}
        )
    except timeout:
        continue
    except ConnectionResetError:
        continue
    open("PolkCounty/" + meeting_id + "-agenda.html", "w").write(response.text)
    time.sleep(1)