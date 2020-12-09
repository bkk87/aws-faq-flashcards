# Download AWS FAQ's as text files for (Anki) flashcard import

This script parses the provided AWS FAQ's and writes each FAQ as a text file.

The format is: `<Question><SeparatorSymbol><Answer>\newline`

Anki is able to import these files by providing the separator symbol.

There are a few rough edges, so please look at each outputted file before importing it. The AWS html pages with the FAQs are not always in the same format. I did not invest the time to work around every "special case".