class HTML:

    resultCode = []

    def __init__(self):
        HTML.resultCode = []

    class body:

        def __enter__(self):
            HTML.resultCode.append("<body>")

        def __exit__(self, *args, **kwargs):
            HTML.resultCode.append("</body>")

    class div:

        def __enter__(self):
            HTML.resultCode.append("<div>")

        def __exit__(self, *args, **kwargs):
            HTML.resultCode.append("</div>")

    def p(self, value):
        tag = "<p>" + value + "</p>"
        HTML.resultCode.append(tag)

    def get_code(self):
        result = ''
        for item in HTML.resultCode:
            result += item
            result += '\n'

        return result


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())

'''
Ождиаемый результат:
<body>
    <div>
        <div>
            <p>Первая строка.</p>
            <p>Вторая строка.</p>
        </div>
        <div>
            <p>Третья строка.</p>
        </div>
    </div>
</body>
'''
