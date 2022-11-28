import httpx
import time

meeting_ids = httpx.get(
    "https://gist.githubusercontent.com/simonw/ad2b938b2e7fb6b7b2289b0f83d1a74f/raw/006b54f804e1bbae280ea5556bff4f888ec99d8d/meeting-ids.json"
).json()
committee = "A9HDX937D70D"

for meeting_id in meeting_ids:
    print(meeting_id)
    response = httpx.post(
        "https://go.boarddocs.com/vsba/fairfax/Board.nsf/PRINT-AgendaDetailed?open",
        data={"id": meeting_id, "current_committee_id": committee}
    )
    open(meeting_id + "-agenda.html", "w").write(response.text)
    time.sleep(1)