#
# Builtin
# Foreground: LightSteelBlue #b0c4de
#
# Comment
# Foreground: chocolate1 #ff7f24
#
# Constant
# Foreground: Aquamarine #7fffd4
#
# Function Name
# Foreground: LightSkyBlue #87cefa
#
# Keyword
# Foreground: Cyan1 #00ffff
#
# String
# Foreground: LightSalmon #ffa07a
#
# Type
# Foreground: PaleGreen #98fb98
#
# Variable Name
# Foreground: LightGoldenrod #eedd82

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

# From Monokai
class EPStyle(Style):
    background_color = "#272822"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                      "#f8f8f2", # class:  ''
        Whitespace:                "",        # class: 'w'
        Error:                     "#960050 bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'

        Comment:                   "#ff7f24", # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   "#00ffff", # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "#00ffff", # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "#98fb98", # class: 'kt'

        Operator:                  "#f92672", # class: 'o'
        Operator.Word:             "",        # class: 'ow'

        Punctuation:               "#f8f8f2", # class: 'p'

        Name:                      "#eedd82", # class: 'n'
        Name.Attribute:            "#a6e22e", # class: 'na' - to be revised
        Name.Builtin:              "#b0c4de", # class: 'nb'
        Name.Builtin.Pseudo:       "",        # class: 'bp'
        Name.Class:                "#a6e22e", # class: 'nc' - to be revised
        Name.Constant:             "#7fffd4", # class: 'no'
        Name.Decorator:            "#a6e22e", # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            "#a6e22e", # class: 'ne'
        Name.Function:             "#87cefa", # class: 'nf'
        Name.Property:             "",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                "#a6e22e", # class: 'nx'
        Name.Tag:                  "#f92672", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised

        Number:                    "#fff", #"#ae81ff", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   "#eedd82", # class: 'l'
        Literal.Date:              "#e6db74", # class: 'ld'

        String:                    "#ffa07a", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "",        # class: 'sc'
        String.Doc:                "",        # class: 'sd' - like a comment
        String.Double:             "",        # class: 's2'
        String.Escape:             "#ae81ff", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "",        # class: 'sr'
        String.Single:             "",        # class: 's1'
        String.Symbol:             "",        # class: 'ss'

        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "#f92672", # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Error:             "",        # class: 'gr'
        Generic.Heading:           "",        # class: 'gh'
        Generic.Inserted:          "#a6e22e", # class: 'gi'
        Generic.Output:            "",        # class: 'go'
        Generic.Prompt:            "",        # class: 'gp'
        Generic.Strong:            "bold",    # class: 'gs'
        Generic.Subheading:        "#75715e", # class: 'gu'
        Generic.Traceback:         "",        # class: 'gt'
    }
