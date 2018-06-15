# tiny-elastic-cli #

A simple cli for querying elasticsearch. Outputs json.

## Config ## 

Launching the cli once will propagate ~/.tiny-elastic-cli.conf

### Installing ###

Global install

`pip install tiny-elastic-cli`

Local install

`pip install --user tiny-elastic-cli`

In the case of local install, the script will be available through `~/.local/bin/elastic` or similar. Consider adding `.local/bin` to your path.

## Usage ##

`elastic --help`

`elastic 'foo:bar'`

`elastic 'foo:bar' --source 'otherfield' | jq .`

## License ##

(The MIT License)

Copyright (c) 2018 Einar Otto Stangvik &lt;einaros@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
