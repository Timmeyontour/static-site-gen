from textnode import TextType, TextNode

def main():
    testNode = TextNode("ABC", TextType.BOLD, "https://www.google.com/search?q=url&rlz=1C1CHBF_deDE925DE980&oq=url&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGDwyBggDEEUYPDIGCAQQRRg8MgYIBRBFGEEyBggGEEUYQTIGCAcQRRhB0gEHMzU1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
    testNode2 = TextNode("ABC", TextType.BOLD, "https://www.google.com/search?q=url&rlz=1C1CHBF_deDE925DE980&oq=url&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGDwyBggDEEUYPDIGCAQQRRg8MgYIBRBFGEEyBggGEEUYQTIGCAcQRRhB0gEHMzU1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
    print(testNode)
    print(testNode2)
    print(testNode == testNode2)

main()