# siqnal gücünü dBm-dən millivata çeviririk: P(mW) = 10^ (dBm / 10)
rsrp_dbm = -95
p_mw = 10 ** (rsrp_dbm / 10)
print(f"{rsrp_dbm} dbm = {p_mw:.2e} mW")
# Bir neçə ölçmə: hansılar zəif siqaldır (< -105 dbm) ?
values = [-85, -97, -110, -102, -118]
for v in values:
    if v < -105:
        print(v, "dbm - zəif siqnal")
    else:
        print(v, "dbm - normal")