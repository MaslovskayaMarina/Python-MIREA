def main(str):
    str = str.replace(" ", "")
    str = str.replace("\n", "")
    result = {}
    i = 0
    k = 0
    while i < len(str):
        resource = ""
        if str[i] == '>' and str[i + 1] == 'd':
            i += 4
            while str[i] != '=':
                resource += str[i]
                i += 1
        if str[i] == '=' and str[i + 1] == '>':
            i += 2
            key = ""
            while str[i] != '.':
                key += str[i]
                i += 1
            result[key] = int(resource)
            k += 1
        i += 1
    return result







main(' <section>def 4277=> usve_227. </section>, <section>def -2769 =>\nedle_659.</section>, <section> def -7441 =>ceon_20. </section>,\n<section>def -378 => erques_870. </section>,')
