def main(s):
    i = 0
    k = 0
    x = ""
    result = {}
    while i < len(s):
        key = ""
        if s[i] == '#':
            i += 1
            while s[i] == ' ':
                i += 1
            while s[i] != ' ' and s[i] != '=':
                x = x + s[i]
                i += 1
        if s[i] == '(':
            i += 1
            while s[i] != ')':
                key = key + s[i]
                i += 1
            result[key] = int(x)
            x = ""
        i += 1
    return result

main("do <section>make#-1666 =>q(vean_848). </section>;<section> make#8965=>q(anlaed_972). </section>; <section>make #9930 => q(onari).</section>; <section>make #-2616=> q(tiusra_980). </section>; od")
