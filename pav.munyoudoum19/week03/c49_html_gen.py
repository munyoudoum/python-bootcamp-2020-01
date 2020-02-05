class HTMLGen():
    def comment(self, cmt):
        return f"<!--{cmt}-->"

    def href(self, link, name):
        return f"<a href=\"{link}\">{name}</a>"

    def title(self, text):
        return f"<title>{text}</title>"

    def body(self, text):
        return f"<body>{text}</body>"

    def div(self, text):
        return f"<div>{text}</div>"

    def p(self, text):
        return f"<p>{text}</p>"
