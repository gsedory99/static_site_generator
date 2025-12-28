class HTML_Node:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f' {key}="{val}"' for key, val in self.props.items()])

    def __repr__(self):
        return f"tag ={self.tag}, value={self.value},children={self.children}, props={self.props}"


class LeafNode(HTML_Node):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTML_Node):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag or not self.children:
            raise ValueError
        children_string = "".join(node.to_html() for node in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
