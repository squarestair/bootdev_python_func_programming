def lines_with_sequence(char):
    def with_char(length):
        def with_length(doc):
            lines = doc.split("\n")
            count = 0
            seq = f"{char}" * int(length)
            for line in lines:
                if seq in line:
                    count += 1
            return count
        return with_length
    return with_char

