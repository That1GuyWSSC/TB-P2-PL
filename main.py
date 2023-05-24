from grammar import Grammar

content = 'start ESCREVER "maria" end'


if __name__ == "__main__":
    g = Grammar()
    g.build()
    res = g.parse(content)