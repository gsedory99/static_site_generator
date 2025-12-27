class HTML_Node:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        formatted_string = ""
        if self.props:
            for key, value in self.props.items():
                formatted_string += f' {key}="{value}"'
        return formatted_string

    def __repr__(self):
        return f"tag ={self.tag}, value={self.value},children={self.children}, props={self.props}"
