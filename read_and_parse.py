import linecache

if __name__ == "__main__":
    txt_file = open("./json_results/Androbugs/8657024da129fc6982f9daa7f3775cf6.txt", "r")
    lines = txt_file.readlines()
    line_counter = 1
    critical = []
    warning = []
    notice = []
    info = []

    critical_status = False
    warning_status = False
    notice_status = False
    info_status = False
    add = True
    for line in lines:
        if line.startswith("[Critical]"):
            critical.append("Critical")
            critical_status = True
            warning_status = False
            notice_status = False
            info_status = False
            add = True
        if line.startswith("[Warning]"):
            warning.append("Warning")
            critical_status = False
            warning_status = True
            notice_status = False
            info_status = False
            add = True
        if line.startswith("[Notice]"):
            notice.append("Notice")
            critical_status = False
            warning_status = False
            notice_status = True
            info_status = False
            add = True
        if line.startswith("[Info]"):
            info.append("Info")
            critical_status = False
            warning_status = False
            notice_status = False
            info_status = True
            add = True
        if line.startswith("-------"):
            add = False
        if critical_status and add:
            critical.append(line_counter)
        if warning_status and add:
            warning.append(line_counter)
        if notice_status and add:
            notice.append(line_counter)
        if info_status and add:
            info.append(line_counter)
        line_counter = line_counter + 1

    #print(critical)
    #print(warning)
    #print(notice)
    #print(info)

    # now let's try to put everything on a JSON format :-)
    json_file = open("./json_results/Androbugs/8657024da129fc6982f9daa7f3775cf6.json", "w")
    #json_file.write("{")
    #json_file.write("\"results\": ")
    json_file.write("{\"M1\": [")
    text2write = ""
    is_first = True
    for critical_line in critical:
        if critical_line == 'Critical' and is_first:
            text2write = text2write + "{\"vulnerability\": \""
            is_first = False
            continue
        if critical_line == 'Critical' and not is_first:
            text2write = text2write + "\", "
            text2write = text2write + "\"details\": \"\", \"severity\": \"Critical\", \"detectedby\": [\"Androbugs\"],"
            text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
            text2write = text2write + "}, {\"vulnerability\": \""
        else:
            what2write = linecache.getline("./json_results/Androbugs/8657024da129fc6982f9daa7f3775cf6.txt", critical_line)
            text2write = text2write + what2write.replace('"', '\\"')[:-1]
    text2write = text2write + "\", "
    text2write = text2write + "\"details\": \"\", \"severity\": \"Critical\", \"detectedby\": [\"Androbugs\"],"
    text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
    text2write = text2write + "}]"
    json_file.write(text2write)
    # print(text2write)
    json_file.write(",")
    json_file.write("\"M2\": [")
    text2write = ""
    is_first = True
    for warning_line in warning:
        if warning_line == 'Warning' and is_first:
            text2write = text2write + "{\"vulnerability\": \""
            is_first = False
            continue
        if warning_line == 'Warning' and not is_first:
            text2write = text2write + "\", "
            text2write = text2write + "\"details\": \"\", \"severity\": \"Warning\", \"detectedby\": [\"Androbugs\"],"
            text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
            text2write = text2write + "}, {\"vulnerability\": \""
        else:
            what2write = linecache.getline("./json_results/Androbugs/8657024da129fc6982f9daa7f3775cf6.txt", warning_line)
            text2write = text2write + what2write.replace('"', '\\"')[:-1]
    text2write = text2write + "\", "
    text2write = text2write + "\"details\": \"\", \"severity\": \"Critical\", \"detectedby\": [\"Androbugs\"],"
    text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
    text2write = text2write + "}]"
    json_file.write(text2write)
    # print(text2write)
    json_file.write(",")
    json_file.write("\"M3\": [")
    text2write = ""
    is_first = True
    for notice_line in notice:
        if notice_line == 'Notice' and is_first:
            text2write = text2write + "{\"vulnerability\": \""
            is_first = False
            continue
        if notice_line == 'Notice' and not is_first:
            text2write = text2write + "\", "
            text2write = text2write + "\"details\": \"\", \"severity\": \"Notice\", \"detectedby\": [\"Androbugs\"],"
            text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
            text2write = text2write + "}, {\"vulnerability\": \""
        else:
            what2write = linecache.getline("./json_results/Androbugs/8657024da129fc6982f9daa7f3775cf6.txt",
                                           notice_line)
            text2write = text2write + what2write.replace('"', '\\"')[:-1]
    text2write = text2write + "\", "
    text2write = text2write + "\"details\": \"\", \"severity\": \"Critical\", \"detectedby\": [\"Androbugs\"],"
    text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
    text2write = text2write + "}]"
    json_file.write(text2write)
    # print(text2write)
    json_file.write(",")
    json_file.write("\"M4\": [")
    text2write = ""
    is_first = True
    for info_line in info:
        if info_line == 'Info' and is_first:
            text2write = text2write + "{\"vulnerability\": \""
            is_first = False
            continue
        if info_line == 'Info' and not is_first:
            text2write = text2write + "\", "
            text2write = text2write + "\"details\": \"\", \"severity\": \"Info\", \"detectedby\": [\"Androbugs\"],"
            text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
            text2write = text2write + "}, {\"vulnerability\": \""
        else:
            what2write = linecache.getline("./json_results/Androbugs/8657024da129fc6982f9daa7f3775cf6.txt",
                                           info_line)
            text2write = text2write + what2write.replace('"', '\\"')[:-1]
    text2write = text2write + "\", "
    text2write = text2write + "\"details\": \"\", \"severity\": \"Critical\", \"detectedby\": [\"Androbugs\"],"
    text2write = text2write + "\"feedback\": [{\"url\":\"\"}, {\"video\":\"\"}, {\"book\":\"\"}, {\"other\":\"\"}]"
    text2write = text2write + "}"
    # print(text2write)
    json_file.write(text2write)
    json_file.write("],")
    json_file.write("\"M5\": [")
    json_file.write("],")
    json_file.write("\"M6\": [")
    json_file.write("],")
    json_file.write("\"M7\": [")
    json_file.write("],")
    json_file.write("\"M8\": [")
    json_file.write("],")
    json_file.write("\"M9\": [")
    json_file.write("],")
    json_file.write("\"M10\": [")
    json_file.write("]")
    json_file.write("}")
    #json_file.write("}")


