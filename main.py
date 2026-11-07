from ingestion import raw
from process import extarct_transforme
from storage import save
from process import geolocation

if __name__ == "__main__":

    rows = raw.toRows('./data')
    all_records = []                  # la LISTE de tous les enregistrements
    rejected = []

    for row in rows:
        row = row.strip()
        if not row:
            continue
        record = extarct_transforme.extract_from_row(row)    # UN enregistrement
        if record is None:
            rejected.append(row)
        else:
            all_records.append(record)   # on ajoute UN élément à LA liste

    print(f"Lignes lues      : {len(rows)}")
    print(f"Lignes extraites : {len(all_records)}")
    print(f"Lignes rejetées  : {len(rejected)}")

    

    save.save_records(all_records)
    save.save_rejected(rejected)

    print("Sauvegarde terminée dans ./storage")

  

ips = {r['ip'] for r in all_records if r['ip']}
countries = {}

for ip in ips:
    info = geolocation.get_location(ip)
    countries[ip] = info.get('country') if info else None

for r in all_records:
    r['country'] = countries.get(r['ip'])