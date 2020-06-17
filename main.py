import arcpy, os

path = "C://SyK//06_GENERAINFO//data"
mdb = "Frecuencias_Model_def_esc.mdb"
table = "Frecuencias_INS_160_export"
info = "frec_interurbanos.info"

f = open(os.path.join(path, info), 'w')

fieldList = ["CODITIN", "HORA1", "FREQ1", "HORA2", "FREQ2", "HORA3", "FREQ3", "HORA4", "FREQ4", "HORA5", "FREQ5",
             "HORA6", "FREQ6", "HORA7", "FREQ7", "HORA8", "FREQ8", "HORA9", "FREQ9", "HORA10", "FREQ10", "HORA11",
             "FREQ11", "HORA12", "FREQ12", "HORA13", "FREQ13", "HORA14", "FREQ14", "HORA15", "FREQ15"]

with arcpy.da.SearchCursor(os.path.join(path, mdb, table), fieldList, sql_clause=(None, "ORDER BY CODITIN")) as cursor:
    for r in cursor:
        i = 0
        line = []
        if i == 0:
            line.append(str(int(r[i])))
            line.append(", ")
            i += 1
        if i == 1:
            while i < 29:
                line.append(str(int(r[i])))
                line.append(", ")
                line.append(str(r[i+1]))
                line.append(", ")
                i = i + 2
        if i == 29:
            line.append(str(int(r[i])))
            line.append(", ")
            line.append(str(r[i + 1]))
            line.append("\n")
        f.writelines(line)
f.close()