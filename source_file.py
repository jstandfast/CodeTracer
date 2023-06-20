class source_file:
    def __init__(self, file_title, file_type, lines):
        self.file_title = file_title
        self.file_type = file_type
        self.lines = lines

    def __str__(self):
        output = f"File: {self.file_title}\n"
        output += f"Lang: {self.file_type}\n"
        output += "Lines:\n"
        i = 1
        for line_content in self.lines:
            output += f"  Line #: {i}: {line_content}"
            i += 1
        return output