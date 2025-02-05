import tokenizer
import parser
import evaluator

def run(text):
    text = "print 3"
    tokens = tokenizer.tokenize(text)
    ast = parser.parse(tokens)
    evaluator.evaluate(ast)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as f:
            source = f.read()
        run(source)
    text = "print 3+3*3"
    run(text)